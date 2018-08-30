import pickle
from get_boxscore_summary import create_boxscore_summaries


bs_data = pickle.load(open('./complete_bs.pkl','rb'))

print(len(bs_data))
f = create_boxscore_summaries(0,-1,['0021201214'],False)

bs_data.update(f)
