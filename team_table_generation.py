import matplotlib as plt
import pandas as pd
import pickle
import seaborn as sns
import numpy as np

def team_data_frame():
    df = pickle.load(open('./big_data/cleaned_table.pkl','rb'))
    td_dict={}
    td_dict['t_id']=[]
    columns = [{1:'team_id', 2:'team_id_home_team'},
     {1:'team_abbreviation', 2:'team_abbreviation_home_team'},
     {1:'team_name', 2:'team_name_home_team'}]
    for c in columns:
        td_dict[c[1]] = []

    for i in range(0, len(df)):
            if df.iloc[i]['team_id_home_team'] not in td_dict: 
                td_dict[df.iloc[i]['team_id_home_team']] = []  
                for c in columns:
                    td_dict[c[1]].append(df.iloc[i][c[2]])

    peedee = pd.DataFrame(td_dict, columns=['team_id','team_abbreviation','team_name'])
    peedee = pickle.dump(peedee,open('./team.pkl','wb'))
    pass

team_data_frame()