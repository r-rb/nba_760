import pickle
import random
from get_boxscore_summary import create_boxscore_summaries
from create_df import pickle_sample

bs_data = pickle.load(open('./complete_bs.pkl','rb'))
no_bs_data = pickle.load(open('./complete_no_bs.pkl','rb'))

for key in bs_data.keys():
    bs_data[key].update(no_bs_data[key])

merged_data = bs_data

print(len(merged_data))

pickle.dump(merged_data,open('./merged_data.pkl','wb'))

pickle_sample(merged_data,20)