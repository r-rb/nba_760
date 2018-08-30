import itertools
ls = ['GAME_DATE_EST',
        'GAME_ID',
        'GAME_SEQUENCE',
        'PTS',
        'PTS_OT1',
        'PTS_OT10',
        'PTS_OT2',
        'PTS_OT3',
        'PTS_OT4',
        'PTS_OT5',
        'PTS_OT6',
        'PTS_OT7',
        'PTS_OT8',
        'PTS_OT9',
        'PTS_QTR1',
        'PTS_QTR2',
        'PTS_QTR3',
        'PTS_QTR4',
        'TEAM_ABBREVIATION',
        'TEAM_CITY_NAME',
        'TEAM_ID',
        'TEAM_NICKNAME',
        'TEAM_WINS_LOSSES']
ots = ['LARGEST_LEAD',
         'LEAD_CHANGES',
         'LEAGUE_ID',
         'PTS_2ND_CHANCE',
         'PTS_FB',
         'PTS_OFF_TO',
         'PTS_PAINT',
         'TEAM_ABBREVIATION',
         'TEAM_CITY',
         'TEAM_ID',
         'TEAM_REBOUNDS',
         'TEAM_TURNOVERS',
         'TIMES_TIED',
         'TOTAL_TURNOVERS']
# ts = ['AST',
#         'BLK',
#         'DREB',
#         'FG3A',
#         'FG3M',
#         'FG3_PCT',
#         'FGA',
#         'FGM',
#         'FG_PCT',
#         'FTA',
#         'FTM',
#         'FT_PCT',
#         'GAME_ID',
#         'MIN',
#         'OREB',
#         'PF',
#         'PLUS_MINUS',
#         'PTS',
#         'REB',
#         'STL',
#         'TEAM_ABBREVIATION',
#         'TEAM_CITY',
#         'TEAM_ID'
#         'TEAM_NAME',
#         'TO']

#ts1 = ['GAME_ID', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS', 'PLUS_MINUS']
ts = ['AST', 'BLK', 'DREB', 'FG3A', 'FG3M', 'FG3_PCT', 'FGA', 'FGM', 'FG_PCT', 'FTA', 'FTM', 'FT_PCT', 'GAME_ID', 'MIN', 'OREB', 'PF', 'PLUS_MINUS', 'PTS', 'REB', 'STL', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'TEAM_ID', 'TEAM_NAME', 'TO']
#print(set(ts2).difference(set(ts)))
#print(f)
ht_convert = lambda t: [x.lower() + '_home_team'  for x in t]
at_convert = lambda t: [x.lower() + '_away_team'  for x in t]

# ht_ls = ht_convert(ls)
# ht_ots = ht_convert(ots)
ht_ts = ht_convert(ts)

# at_ls = at_convert(ls)
# at_ots = at_convert(ots)
at_ts = at_convert(ts)

# print(ht_ls)
# print(ht_ots)
print(ht_ts) 
# print(at_ls) 
# print(at_ots)
print(at_ts) 