import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import datetime as dt

def plot_player(pid,df):

    rows = df.loc[df['player_id'] == pid]

    plt.plot(rows["game_date"],rows["pts"],'ro')
    plt.title(" Points in a game vs Game Date")
    plt.show()
    #print(rows)

    pass

pid = "2544"
df = pd.read_pickle('../pickled_data/player_game_stats.pkl')

# df["game_date"] = pd.to_datetime(df["game_date"])

# df.sort_values("game_date",inplace = True, ascending = False)
# print(df["game_date"])

# df = pickle.dump(df,open('./player_game_stats.pkl','wb'))

plot_player(pid,df)
