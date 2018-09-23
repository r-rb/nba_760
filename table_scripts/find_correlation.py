import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import datetime as dt
import pprint as pp

df = pd.read_pickle('../data_types_resolved.pkl')
game_df = pd.read_pickle('../game.pkl')

def changePklValues(): 
    df['fantasy_points'] = pd.to_numeric(df['fantasy_points'], errors='coerce')
    df['pts'] = pd.to_numeric(df['pts'], errors='coerce')
    df['blk'] = pd.to_numeric(df['blk'], errors='coerce')
    df['reb'] = pd.to_numeric(df['reb'], errors ='coerce')
    df['fga'] = pd.to_numeric(df['fga'], errors ='coerce')
    df['fgm'] = pd.to_numeric(df['fgm'], errors ='coerce')
    df['ft_pct'] = pd.to_numeric(df['ft_pct'], errors ='coerce')
    df['days_since_injury'] = pd.to_numeric(df['days_since_injury'], errors ='coerce')
    df['fta'] = pd.to_numeric(df['min'], errors ='coerce')
    df['pf'] = pd.to_numeric(df['pf'], errors ='coerce')
    df['fg3a'] = pd.to_numeric(df['fg3a'], errors ='coerce')
    df['fg3m'] = pd.to_numeric(df['fg3m'], errors ='coerce')
    df['pf'] = pd.to_numeric(df['pf'], errors ='coerce')
    df['stl'] = pd.to_numeric(df['stl'], errors ='coerce')

    df.to_pickle('data_types_resolved.pkl')


y = ['ast','blk','dreb','fg3_pct','fg3a','fg3m','fg_pct','fga','fgm','ft_pct','fta','ftm','min','oreb','pf','plus_minus','pts','reb','stl','to','last_inj','fantasy_points']

# x =  df[y[1:]].corr(df['fantasy_points'])

p=df.corr(method="spearman")
# z = list(map(lambda x: df[x].corr( df['fantasy_points']), y ))
p = (p['fantasy_points'])
pp.pprint(p[1:21])


plt.bar(y,p)
plt.title('Correlation of input features vs fantasy points')
plt.xlabel('Input features')
plt.ylabel('Target feature (Fantasy points)')
plt.show()