import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import datetime as dt

df = pd.read_pickle('./player_game_stats.pkl')
print(len(df))

df.comment = df.comment.fillna('')
subdf = df

subdf = subdf[subdf["comment"].str.contains("DNP",na = False) | subdf["comment"].str.contains("NWT",na = False) |  subdf["comment"].str.contains("DND",na = False)]
subdf = subdf[subdf["ast"].isnull()|subdf["pts"].isnull()]
print(subdf["comment"])
