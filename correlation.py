import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import datetime as dt
import pprint as pp
import pandas as pd
from scipy.stats.stats import pearsonr   


df = pd.read_pickle('./data_types_resolved.pkl')
game_df = pd.read_pickle('./game.pkl')

y = ['ast','blk','dreb','fg3_pct','fg3a','fg3m','fg_pct','fga','fgm','ft_pct',
    'fta','ftm','min','oreb','pf','plus_minus','pts','reb','stl','to','days_since_injury','fantasy_points']

def create_input_features(pid, n, df, feats):
    rows = df.loc[ df['player_id'] == pid]
    rows = rows.sort_values("game_date")
    X = np.zeros(( (len(rows) - (n), 1 + (len(feats)*n)) ))
    y= np.zeros((len(rows) - (n)))
    for i in range(n, (len(rows) - 1)):
        last_n = rows.iloc[(i - n) : i]
        X[(i - n),0] = pid
        for a,feat in enumerate(feats):
            start_idx = a*n +1
            end_idx = start_idx + n
            X[(i - n),start_idx:end_idx] = last_n[feat].tolist()
        y[(i - n)] = rows.iloc[i]["fantasy_points"]
    return X, y
    
def boruto(X,y, n):


inp, z = (create_input_features('201935', 5, df, y))
boruto(inp,z,5)
            



