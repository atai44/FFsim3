import numpy as np
import random
from sleeper_wrapper import League
from sleeper import get_scorelists, get_schedules

league_id = 723665944777388032
league = League(league_id)

# names_to_scores = get_scorelists(league)
# names_to_scheds = get_schedules(league)
# ex_scores = list(names_to_scores.items())[0][1]
# week = np.where(ex_scores==0)[0][0]

def reset_scores(week, names_to_scores):
    #reset team scores to 0 starting from week
    for name,scores in names_to_scores.items():
        names_to_scores[name][week:] = 0
        
def sim_scores(week, names_to_scores):
    #simulate team scores starting from week
    for name, scores in names_to_scores.items():
        mean = np.mean(scores[:week])
        std = np.std(scores[:week])
        print(name, mean, std)
        names_to_scores[name][week:] = np.random.normal(mean,std,len(scores)-week)