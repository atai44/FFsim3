from sleeper_wrapper import League

league_id = 723665944777388032
league = League(league_id)
users = league.get_users()
rosters = league.get_rosters()
standings = league.get_standings(rosters,users)

rosters_to_users = league.map_rosterid_to_ownerid(rosters)
users_to_names = league.map_users_to_team_name(users)

def print_scoreboard(league):
    for i in range(1,15):
        matchups = league.get_matchups(i)
        matchups = sorted(matchups, key = lambda x:x["matchup_id"])
        print(f"Week {i}")
        # for m in matchups:
        #     print(users_to_names[rosters_to_users[m["roster_id"]]], m["points"])
        
        for i in range(0,12,2):
            print(users_to_names[rosters_to_users[matchups[i]["roster_id"]]], matchups[i]["points"], "vs", users_to_names[rosters_to_users[matchups[i+1]["roster_id"]]], matchups[i+1]["points"])
        print()
        
def get_scorelists(league):
    
    #make a dictionary called names_to_scores from team names to empty np arrays
    
    for i in range(1,15):
        matchups = league.get_matchups(i)
        print(f"Week {i}")
        for m in matchups:
            #fill in arrays
    #return the dict
            
def get_schedules(league):
    
    #make a dictionary called names_to_scheds from team names to empty np arrays
    
    for i in range(1,15):
        matchups = league.get_matchups(i)
        print(f"Week {i}")
        for m in matchups:
            #fill in arrays
    #return the dict
        
    
print_scoreboard(league)
    
    
