from sleeper_wrapper import League

league_id = 723665944777388032
league = League(league_id)
users = league.get_users()
rosters = league.get_rosters()
standings = league.get_standings(rosters,users)

rosters_to_users = league.map_rosterid_to_ownerid(rosters)
users_to_names = league.map_users_to_team_name(users)

for i in range(1,15):
    matchups = league.get_matchups(i)
    print(f"Week {i}")
    for m in matchups:
        print(users_to_names[rosters_to_users[m["roster_id"]]], m["points"])
    print()
    
    
