import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import datetime as dt
import pprint as pp
df = pd.read_pickle('../pickled_data/player_game_stats.pkl')
print(len(df))

df.comment = df.comment.fillna('')
subdf = df

bad_pids = [204040, 'Matt Freije', 'George Lynch', 'P.J. Brown', 'Junior Harrington', 'David Wesley', 'Dan Dickau', 'Chris Andersen',\
            'JR Smith', 'Corsley Edwards', 'Lonny Baxter', 'Alex Garcia', 'Jamaal Magloire', 'Lee Nailon', 'David West', 'Gerald Wallace',\
            'Emeka Okafor', 'Primoz Brezec', 'Keith Bogans', 'Brevin Knight', 'Melvin Ely', 'Kareem Rush', 'Jason Kapono', 'Jason Hart',\
            'Jamal Sampson', 'Steven Smith', 'Theron Smith', 'Eddie House', 'Tamar Slay', 'Jahidi White', 203942,203942, 1628454, 204040,\
                101252, 203942, 1628473, 203942, 203942, 203942, 203942, 203942, 2773, 201183, 201204, 1628473]
bad_pids = [str(x) for x in bad_pids]
subdf = subdf[~(subdf["player_id"].isin(bad_pids))]

#pp.pprint( df[df["comment"].str.contains("DND",na = False) & ~df["comment"].str.contains("Coach's Decision",na = False)][["comment","pts","ast",]])

subdf.to_pickle('../pickled_data/preprocess_injuries.pkl')

#subdf = subdf[~subdf["comment"].str.contains("DNP",na = False) | \
#                         ~subdf["comment"].str.contains("NWT",na = False) | \
#                              ~subdf["comment"].str.contains("DND",na = False)]
# subdf = subdf[subdf["ast"].notnull()|subdf["pts"].notnull()]


# subdf.to_pickle('./player_game_stats_cleaned.pkl')
