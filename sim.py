import numpy as np
import random
import pandas as pd
from sleeper_wrapper import League
from sleeper import get_scorelists, get_schedules

#assumes no ties and that no team scores 0 points in any week

#setup, only needed once
league_id = 723665944777388032
league = League(league_id)
names_to_scores = get_scorelists(league)
names_to_scheds = get_schedules(league)
ex_scores = list(names_to_scores.items())[0][1]
week = np.where(ex_scores==0)[0][0]
data = {'Wins': np.zeros(12), 'Points For': np.zeros(12), 1: np.zeros(12), 2: np.zeros(12), 3:np.zeros(12), 4:np.zeros(12), 5:np.zeros(12), 6:np.zeros(12), 7:np.zeros(12), 8: np.zeros(12), 9:np.zeros(12), 10:np.zeros(12), 11:np.zeros(12), 12:np.zeros(12), 'Wild Card':np.zeros(12)}
df = pd.DataFrame(data, index = list(names_to_scores.keys()))
places = ['1st', '2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th']

def reset_scores(week, names_to_scores):
    #reset team scores to 0 starting from week
    for name,scores in names_to_scores.items():
        names_to_scores[name][week:] = 0
        
def sim_scores(week, names_to_scores):
    #simulate team scores starting from week
    for name, scores in names_to_scores.items():
        mean = np.mean(scores[:week])
        std = np.std(scores[:week])
        names_to_scores[name][week:] = np.random.normal(mean,std,len(scores)-week)
        
def fill_df(df, names_to_scheds, names_to_scores):
    #fills the dataframe to be sorted
    
    #fill in pf
    for name, scores in names_to_scores.items():
        df.at[name,'Points For'] = np.sum(scores[:14])
        
    #fill in wins
    for name, sched in names_to_scheds.items():
        w = 0
        for i in range(len(sched)):
            if names_to_scores[name][i] > names_to_scores[sched[i]][i]: 
                w = w+1
                if (name == "InsertCoolName"): print(sched[i])
        df.at[name, 'Wins'] = w

def process_results(df):
    #calculates rankings and playoff outcomes
    df.sort_values(by=['Wins', 'Points For'], ascending=False, inplace=True)