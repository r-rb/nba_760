import pickle
from get_boxscore_summary import create_boxscore_summaries

paths = ["./data/bs_summaries_6000_12000.pkl","./data/bs_summaries_0_6000.pkl","./data/bs_summaries_12000_-1.pkl"]
game_ids = pickle.load(open('./data/game_id_list.pkl','rb'))
total ={}
for p in paths:
    total.update(pickle.load(open(p,'rb')))

new_data = [x for x in game_ids if x not in list(total.keys())]

nd =create_boxscore_summaries(0,-1,new_data,False)

total.update(nd)

print(len(total))

pickle.dump(total,open('./complete_bs.pkl','wb'))


    