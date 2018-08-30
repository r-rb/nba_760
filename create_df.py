import pickle
import random
import pandas as pd
import pprint as pp
import itertools
import time
from random_scripts.processing_constants import *


def load_raw_data():
	return pickle.load(open('./data/game_data_total.pkl','rb'))

def load_sample_data():
	return pickle.load(open('./data/sample_data.pkl','rb'))

def pickle_sample(data,sample_size = 10):
	pickle.dump({k:data[k] for k in random.sample(list(data.keys()),sample_size)},open('./data/sample_data.pkl','wb'))

def gamestat_columns(entry,game_stats):
	values = []
	for st in game_stats:
		if st == 'lastmeeting' and entry[st] == []:
			values += [None] * 12
			continue
		values += [entry[st][0][k] for k in sorted(entry[st][0].keys())]
	
	return values

def playerstat_columns(entries,home_team_id,away_team_id,need_cols = True):
	values	= []
	ht = [x for x in entries if x["TEAM_ID"] == home_team_id]
	at = [x for x in entries if x["TEAM_ID"] == away_team_id]
	extract_values = lambda t: itertools.chain.from_iterable([ [t[i][k] for k in sorted(t[i].keys()) ] if i < len(t) else [None] * len(t[0]) for i in range(0,15) ])
	values += extract_values(ht)
	values += extract_values(at) 

	return values

def teamstat_columns(entry,team_specific_stats,home_team_id,away_team_id):
	values	= []
	for st in team_specific_stats:
		ht = [x for x in entry[st] if x["TEAM_ID"] == home_team_id]
		at = [x for x in entry[st] if x["TEAM_ID"] == away_team_id]
		values += [ht[0][k] for k in sorted(ht[0].keys())]
		values += [at[0][k] for k in sorted(at[0].keys())]

	return values

if __name__ == '__main__':
	t0 = time.time()
	data = pickle.load(open('./merged_data.pkl','rb'))
	t1 = time.time()
	
	print(' ######################################################################### ')
	print(' Loading in raw game data took: ' + str(round(t1 -t0))  + ' seconds')
	
	game_stats = ['gameinfo','lastmeeting']
	team_specific_stats = ['linescore','otherstats','teamstats']
	cols = game_stat_cols + home_team_cols + away_team_cols + home_team_linescore \
			+ away_team_linescore + home_team_otherstats + away_team_otherstats + home_team_teamstats + away_team_teamstats

	flattened_data = { gid:[] for gid in data }

	for gid in data:
		entry = data[gid]
		home_team_id = entry["gamesummary"][0]["HOME_TEAM_ID"]
		away_team_id = entry["gamesummary"][0]["VISITOR_TEAM_ID"]

		v1 = gamestat_columns(entry,game_stats)
		v2 = playerstat_columns(entry["playerstats"],home_team_id,away_team_id)
		v3 = teamstat_columns(entry,team_specific_stats,home_team_id,away_team_id)

		flattened_data[gid].extend(v1+v2+v3)

	t2 = time.time()

	print(' ######################################################################### ')
	print(' Flattening to file took: ' + str(round(t2 -t1))  + ' seconds')

	df = pd.DataFrame.from_dict(flattened_data, orient='index')
	df.columns = cols
	
	print(df.head())

	
	pickle.dump(df,open('./complete_df.pkl','wb'))

	print(' ######################################################################### ')
	print(' Making and dumping dataframe to file took: ' + str(round(time.time() -t2))  + ' seconds')
