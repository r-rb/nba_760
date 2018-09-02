import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
import datetime as dt
import pprint as pp

def remove_non_injuries():
    # Data with no bad pids:
    df = pd.read_pickle("../pickled_data/preprocess_injuries.pkl")

    print(len(df))
    # Removing DNP's that have coach
    df = df[~(df["comment"].str.lower().str.contains('dnp',na = False) & (df["comment"].str.lower().str.contains('coach',na = False) | df["comment"].str.lower().str.contains('suspen',na = False) | df["comment"].str.lower().str.contains('personal',na = False)  ))]

    # Removing DND that have coach
    df = df[~(df["comment"].str.lower().str.contains('dnd',na = False) & (df["comment"].str.lower().str.contains('coach',na = False) | df["comment"].str.lower().str.contains('suspen',na = False) | df["comment"].str.lower().str.contains('personal',na = False) ))]

    # Removing NWT that have suspend or personal
    df = df[ ~(df["comment"].str.lower().str.contains('nwt',na = False) & (df["comment"].str.lower().str.contains('suspen',na = False) | df["comment"].str.lower().str.contains('personal',na = False) ) )]

    # Sort by date in ascending order for easy travesal
    df = df.sort_values("game_date",ascending = True)

    df.to_pickle('../pickled_data/PGS_without_non_injuries.pkl')

def add_injury_col():
    df = pd.read_pickle('../pickled_data/PGS_without_non_injuries.pkl')
    df = df.sort_values("game_date",ascending = True)
    n_rows = len(df)
    injury_counter = {pid:{} for pid in list(set(df.player_id))}
    inj_column = [-1] * n_rows 
    season_column = [""] * n_rows

    get_season = lambda x: f'{(x.year-1)}-{(x.year)}' if (x.month < 5) else f'{(x.year)}-{(x.year+1)}'

    for i in range(n_rows):
        # Info for a row
        if not(i%1000):
            print(i)
            
        pid = df.iloc[i]["player_id"]
        season = get_season(df.iloc[i]["game_date"])
        has_injury = True if len(df.iloc[i]["comment"]) > 1 else False
        date = df.iloc[i]["game_date"]

        if has_injury:
            injury_counter[pid][season] = date
            days_since_injury = 0
        else:
            if season not in injury_counter[pid]:
                days_since_injury = -1
            else:
                days_since_injury = pd.Timedelta(date - injury_counter[pid][season]).days
        season_column[i] = season
        inj_column[i] = days_since_injury
            
    df["days_since_injury"] = inj_column
    df["season"] = season_column

    print(df[df["player_id"] == '201935'][["days_since_injury","season"]])

        

def main():
    # remove_non_injuries()
    add_injury_col()


if __name__ == '__main__':
    main()






