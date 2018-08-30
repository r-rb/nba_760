import matplotlib as plt
import pandas as pd
import pickle
import seaborn as sns
import numpy as np
import pprint as pp

def make_player_game(df):
    team_types = '_away_team_','_home_team_'

    player_cols = ['ast', 'blk','comment', 'dreb', 'fg3a','fg3m','fg3_pct', 'fga', 'fgm', 'fg_pct', 'fta','ftm','ft_pct', 'game_id', 'min', 'oreb', 'pf', 'player_id','player_name','plus_minus','pts', 'reb', 'start_position','stl', 'team_abbreviation','team_city', 'team_id', 'to']    
    ps_dict = {} # init
    ps_dict['gid'] = []

    for c in player_cols:
        ps_dict[c] = []

    for idx, row in df.iterrows():
        gid = row["game_id"]
        for tt in team_types:
            for n in range(1,16):
                if not pd.isnull(row["player_id" + tt + str(n)]):
                    ps_dict["gid"].append(gid)
                    for c in player_cols:
                        col = c + tt + str(n)
                        ps_dict[c].append(row[col])
    
    new_df = pd.DataFrame.from_dict(ps_dict)
    pp.pprint(ps_dict)
    pickle.dump(new_df,open("./player_game_stats.pkl","wb"))
                    
df = pickle.load(open('./complete_df.pkl','rb'))

make_player_game(df)

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