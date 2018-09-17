import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import datetime as dt

def plot_player(pid,df):

    rows = df.loc[ (df['player_id'] == pid) & (df["season"] == "2015-2016") ]

    plt.plot(rows["game_date"],rows["fantasy_points"],'-ro')
    plt.title(" Fantasy oints in a game vs Game Date")
    plt.show()
    #print(rows)


def plot_player_vs_team(pid,tid,season,df,game_df):
    rows = df.loc[(df["season"]== season) & (df['player_id'] == pid)]
    game_rows = game_df.merge(rows, left_on = 'game_id', right_on='game_id', how='inner')
    game_rows = game_rows[(game_rows.home_team_id == tid) | (game_rows.away_team_id == tid)]

    print(game_rows)

    game_rows.sort_values("game_date_x",inplace = True)

    plt.plot(game_rows["game_date_x"],game_rows["fantasy_points"],'-ro')
    plt.show()

def plot_player_vs_team_seasons(pid,tid,season_list,df,game_df):
    rows = df[(df.season.isin(season_list)) & (df.player_id == pid)]
    game_rows = game_df.merge(rows, left_on = 'game_id', right_on='game_id', how='inner')
    game_rows = game_rows[(game_rows.home_team_id == tid) | (game_rows.away_team_id == tid)]

    print(game_rows)

    game_rows.sort_values("game_date_x",inplace = True)

    plt.plot(game_rows["game_date_x"],game_rows["fantasy_points"],'-ro')
    plt.show()

    #game_rows = rows.loc[ (game_df.loc[rows["game_id"]]["home_team_id"] == tid) | (game_df.loc[rows["game_id"]]["away_team_id"] == tid)]

    #print(game_ids)

pid = "201935"
tid = "1610612744"
season = "2016-2017"
season_list = ["2016-2017","2017-2018","2015-2016"]
df = pd.read_pickle('../pickled_data/pgs_table_done.pkl')
game_df = pd.read_pickle('../pickled_data/game.pkl')

plot_player_vs_team_seasons(pid,tid,season_list,df,game_df)
# df["game_date"] = pd.to_datetime(df["game_date"])

# df.sort_values("game_date",inplace = True, ascending = False)
# print(df["game_date"])

# df = pickle.dump(df,open('./player_game_stats.pkl','wb'))

#plot_player(pid,df)
