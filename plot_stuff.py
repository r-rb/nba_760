import matplotlib as plt
import pandas as pd
import pickle
import seaborn as sns
import numpy as np

def player_lookup(pid,season):
    pass


df = pickle.load(open('./complete_df.pkl','rb'))

print(df.head())

print(type(df["last_game_home_team_id"].iloc[0]))

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



