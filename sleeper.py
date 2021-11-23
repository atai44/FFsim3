from sleeper_wrapper import League
import numpy as np

# league_id = 723665944777388032
# league = League(league_id)
# users = league.get_users()
# rosters = league.get_rosters()

# rosters_to_users = league.map_rosterid_to_ownerid(rosters)
# users_to_names = league.map_users_to_team_name(users)

def get_info(league):
    #returns basic information about league
    
    users = league.get_users()
    rosters = league.get_rosters()
    rosters_to_users = league.map_rosterid_to_ownerid(rosters)
    users_to_names = league.map_users_to_team_name(users)
    return users,rosters,rosters_to_users,users_to_names

def print_scoreboards(league):
    #prints every matchup of every week
    
    #setup
    users,rosters,rosters_to_users,users_to_names = get_info(league)
    
    #print matchups
    for i in range(1,18):
        matchups = league.get_matchups(i)
        matchups = sorted(matchups, key = lambda x:x["matchup_id"])
        print(f"Week {i}")
        # for m in matchups:
        #     print(users_to_names[rosters_to_users[m["roster_id"]]], m["points"])
        
        for i in range(0,12,2):
            print(users_to_names[rosters_to_users[matchups[i]["roster_id"]]], matchups[i]["points"], "vs", users_to_names[rosters_to_users[matchups[i+1]["roster_id"]]], matchups[i+1]["points"])
        print()
        
def get_scorelists(league):
    #returns a dict mapping team names to np array of scores
    
    #setup
    users,rosters,rosters_to_users,users_to_names = get_info(league)
    names_to_scores = {}
    for user,name in users_to_names.items():
        names_to_scores[name] = np.zeros(17)
        
    #fill in scores
    for i in range(1,18):
        matchups = league.get_matchups(i)
        for m in matchups:
            name = users_to_names[rosters_to_users[m["roster_id"]]]
            names_to_scores[name][i-1] = m["points"]
        
    return names_to_scores
            
def get_schedules(league):
    #returns a dict mapping team names to np array of strings representing schedule
    
    #setup
    users,rosters,rosters_to_users,users_to_names = get_info(league)
    names_to_scheds = {}
    for user,name in users_to_names.items():
        names_to_scheds[name] = np.array(range(14), dtype='<U16')
        
    #fill in schedules
    for i in range(1,15):
        matchups = league.get_matchups(i)
        matchups = sorted(matchups, key = lambda x:x["matchup_id"])
        for j in range(0,12,2):
            team1 = users_to_names[rosters_to_users[matchups[j]["roster_id"]]]
            team2 = users_to_names[rosters_to_users[matchups[j+1]["roster_id"]]]
            names_to_scheds[team1][i-1] = team2
            names_to_scheds[team2][i-1] = team1
    
    return names_to_scheds
        
    
    
    
