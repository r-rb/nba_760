import matplotlib as plt
import pandas as pd
import pickle
import seaborn as sns
import numpy as np
import pprint as pp

def player_game_info(df):

    team_types = '_away_team_','_home_team_'

    player_cols = ['ast', 'blk','comment', 'dreb', 'fg3a','fg3m','fg3_pct', 'fga', 'fgm', 'fg_pct', \
                    'fta','ftm','ft_pct', 'game_id', 'min', 'oreb', 'pf', 'player_id','player_name','plus_minus','pts',\
                        'reb', 'start_position','stl', 'team_abbreviation','team_city', 'team_id', 'to']    
    
    ps_dict = {}
    ps_dict['gid'] = []
    ps_dict["game_date"] =[]
    for c in player_cols:
        ps_dict[c] = []

    count=0

    for _, row in df.iterrows():
        if not(count% 100):
            print(count)
        count += 1
        gid = row["game_id"]
        game_date = row["game_date"]
        for tt in team_types:
            for n in range(1,16):
                if not pd.isnull(row["player_id" + tt + str(n)]):
                    ps_dict["gid"].append(gid)
                    ps_dict["game_date"].append(game_date)
                    for c in player_cols:
                        col = c + tt + str(n)
                        ps_dict[c].append(row[col])
    
    new_df = pd.DataFrame.from_dict(ps_dict)
    pickle.dump(new_df,open("./player_game_stats.pkl","wb"))

def game_info_table(df):

    team_types = '_away_team','_home_team'

    player_cols = ['largest_lead', 'lead_changes', 'league_id', 'pts_2nd_chance', 'pts_fb', 'pts_off_to', \
    'pts_paint', 'team_city', 'team_id', 'team_rebounds', 'team_turnovers', 'times_tied', \
    'total_turnovers','ast', 'blk', 'dreb', 'fg3a', 'fg3m', 'fg3_pct', 'fga', 'fgm', 'fg_pct', 'fta', 'ftm', 'ft_pct', 'game_id',\
     'min', 'oreb', 'pf', 'plus_minus', 'pts', 'reb', 'stl', 'team_abbreviation', 'team_city', 'team_id', 'team_name', 'to']
    player_cols = list(set(player_cols))
    ps_dict = {}
    ps_dict['gid'] = []

    for c in player_cols:
        ps_dict[c] = []

    count=0

    for _, row in df.iterrows():
        if not(count% 100):
            print(count)
        count += 1
        gid = row["game_id"]
        game_date = row["game_date"]
        for tt in team_types:
            ps_dict["gid"].append(gid)
            for c in player_cols:
                col = c + tt
                val = row[col]
                try:
                    val = row[col].iloc[0]
                except Exception:
                    pass
                ps_dict[c].append(val)
    
    new_df = pd.DataFrame.from_dict(ps_dict)
    pickle.dump(new_df,open("./team_game_stats.pkl","wb"))
    print(new_df)

def team_data_frame():
    #My shit code
    df = pickle.load(open('./cleaned_table.pkl','rb'))
    td_dict={}
    td_dict['t_id']=[]
    columns = [{1:'team_id', 2:'team_id_home_team'},
     {1:'team_abbreviation', 2:'team_abbreviation_home_team'},
     {1:'team_name', 2:'team_name_home_team'}]
    for c in columns:
        td_dict[c[1]] = []

    for i in range(0, len(df)):
            if df.iloc[i]['team_id_home_team'] not in td_dict and df.iloc[i]['team_id_home_team'] != 'Bobcats': 
                td_dict[df.iloc[i]['team_id_home_team']] = []  
                for c in columns:
                    td_dict[c[1]].append(df.iloc[i][c[2]])

    df = pd.DataFrame(td_dict, columns=['team_id', 'team_abbreviation', 'team_name'])
    print(df)
    pickle.dump(df,open('./team.pkl','wb'))
    pass

def player_table():
    pass

def game_table():
    
    df = pickle.load(open('./cleaned_table.pkl','rb'))
    td_dict={}
    td_dict['game_id']=[]
    columns = [{1:'game_id', 2:'game_id'},
     {1:'home_team_id', 2:'team_id_home_team'},
     {1:'away_team_id', 2:'team_id_away_team'},
     {1:'winning_team_id', 2:'winning_team_id'},
     {1:'game_date', 2:'game_date'}]
    for c in columns:
        td_dict[c[1]] = []

    count = 0
    for i in range(0, len(df)):
        if not(count% 100):
            print(count)

        count += 1
        if df.iloc[i]['game_id'] not in td_dict: 
            td_dict[df.iloc[i]['game_id']] = []  
            for c in columns:
                if c[1] == 'winning_team_id':
                    td_dict[c[1]].append(df.iloc[i]['team_id_home_team'] if df.iloc[i]['pts_home_team_1'] > df.iloc[i]['pts_away_team_1'] else df.iloc[i]['team_id_away_team'])
                else:
                    td_dict[c[1]].append(df.iloc[i][c[2]])

    df = pd.DataFrame(td_dict, columns=['game_id', 'home_team_id', 'away_team_id', 'winning_team_id', 'game_date'])
    print(df)
    pickle.dump(df,open('./game.pkl','wb'))
    pass

#df = pickle.load(open('./complete_df.pkl','rb'))
game_table()



# game_info_table(df)

#pid_list = pickle.load(open('./data/player_set.pkl','rb'))

# subdf = df.head()

# pickle.dump(subdf,open("./sub_df.pkl","wb"))

# print(df.head())
# print(type(df["last_game_home_team_id"].iloc[0]))

# df = df.loc[:,~df.columns.duplicated()]
# df.index = df['game_id']
# df.fillna(value=np.nan, inplace=True)

# id_cols = [x for x in df.columns if 'id' in x]
# df[id_cols] = df[id_cols].astype(str)
# df["game_date"] = pd.to_datetime(df["game_date"])

# drop_dates = [x for x in df.columns if not(x == "game_date") and "game_date" in x]

# df.drop(drop_dates,axis=1, inplace=True)

# print(df["game_date"])

# df = pickle.dump(df,open('./complete_df.pkl','wb'))

#print(df.dtypes)