# FFsim3

Instructions:

Install sleeper api wrapper (https://github.com/SwapnikKatkoori/sleeper-api-wrapper#install)

In console, run sim.py

In console, call run_sim(N, week, names_to_scores, names_to_scheds, df) where N is the number of simulations to run (leave the rest alone)

Notes:

Because Sleeper has a bug involving the changing of scoring settings, I use a .csv to get the scores. 

Getting the schedules is very slow.

The simulation is very slow. N=1000 takes a few seconds on my machine.

To Do:

Write results to output .csv

Write function to automatically update the csv of scores with changed usernames and scores of the latest week
