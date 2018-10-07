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
import pandas as pd

def scrape_matchups(): 
    
    df = pd.read_pickle('./player_game_table.pkl')
    seasons = ["2017-2018", "2016-2017", "2015-2016"]
    #print(df.head(1))
    game_ids = df.loc[(df.player_id == "2544") & (df.season.isin(seasons))]
    player_ids = set([])
    count = 0
    for idx, row in game_ids.iterrows():
        if not count%10:
            print(count, " out of ", game_ids.shape)
        count += 1
        
        all_games = df.loc[(df.game_id == row.game_id) & (df.team_id != row.team_id)]
        #print(all_games)
        for idx, game_row in all_games.iterrows():
            player_ids.add(game_row.player_id)

    print(len(player_ids))
    print(player_ids)
    api_seasons = ["2017-18", "2016-17", "2015-16"]
    headers = ['player_id', 'min', 'fgm', 'fga', 'fg3m', 
    'fg3a', 'ftm', 'fta', 'oreb', 'dreb', 'reb', 'ast', 'tov','stl', 'blk', 'pts', 'season', 'player_vs_id', 'fp']
    not_input = {}
    for header in headers:
        not_input[header] = []

    count = 0
    for player_id in player_ids:
        count += 1
        if ~count%10:
            print(count, " out of ", len(player_ids))
        for season in api_seasons:
            response = player.PlayerVsPlayer(2544,player_id, season=season).json
            for header in headers:
                if header.upper() in response['resultSets'][0]['headers']:
                    idx = response['resultSets'][0]['headers'].index(header.upper())
                    not_input[header].append(str(response['resultSets'][0]['rowSet'][0][idx]))
                
            #add FP
            not_input['season'].append(season)
            not_input['player_vs_id'].append(player_id)
            not_input['fp'].append('meme')  

    #pp.pprint(response['resultSets'][0])
    df = pd.DataFrame(data=not_input)
    df.to_pickle('./player_vs_table.pkl')

scrape_matchups()
	

