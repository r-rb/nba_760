from nba_py import player
from nba_py.player import get_player
from nba_py import constants
from nba_py import team
from nba_py import game
from nba_py.constants import TEAMS

import pickle
import re
import time
import json
import pprint as pp
import sys


def convert_game_ids(set_of_gid):
	now_a_list = list(set_of_gid)
	pickle.dump(now_a_list,open('./data/game_id_list.pkl','wb'))

def create_boxscore_summaries(start=0 ,end = -1,game_ids = False,save_dict=True):

	if not game_ids:
		game_ids = pickle.load(open('./data/game_id_list.pkl','rb'))[start:end]

	num_gid = len(game_ids)

	print(game_ids[0:5])

	filename = './data/bs_summaries_{start}_{end}.pkl'.format(start =start,end =end)
	database = {}

	t0 = time.time()

	for idx,gid in enumerate(game_ids):
		
		try:
			response = game.BoxscoreSummary(gid).json
		except Exception as err:
			print('Got an error at idx of ' + str(idx) + ' with message: ' + str(err))
			continue
			
		entry = {}
		
		for rs in response["resultSets"]:
			entry[rs["name"].lower()] = []
			for rk in rs["rowSet"]:
				entry[rs["name"].lower()].append({n:r for n,r in zip(rs["headers"],rk)})

		database[gid] = entry

		if not (idx+1) % 100 or not idx :
			print('Just completed: ' + str(idx + 1) + ' of ' + str(num_gid) + ' with an ETC of ' +  str( ((time.time() - t0)/(idx+1)) * (num_gid - (idx+1) )))
			pickle.dump(database,open(filename,'wb'))
	if save_dict:
		pickle.dump(database,open(filename,'wb'))
	else:
		return database
	
if __name__ == '__main__':

	create_boxscore_summaries(int(sys.argv[1]),int(sys.argv[2]))
