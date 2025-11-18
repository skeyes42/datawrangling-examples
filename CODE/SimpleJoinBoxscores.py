# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_5_SimpleJoinBoxscores.py
# DATE 2025-10-19
# DESCRIPTION: 

import sqlite3
import os
import pandas as pd

path_to_database = os.path.join(
    os.getenv("EXAMPLES"), "Boxscores.db")

# Connect to database
con = sqlite3.connect(path_to_database)

# Read tables into DataFrames
boxscores = pd.read_sql_query("SELECT * FROM Boxscores", con)
players = pd.read_sql_query("SELECT * FROM Players", con)
teams = pd.read_sql_query("SELECT * FROM Teams", con)

# Rename columns
players = players.rename(columns={'PLAYER_NAME': 'Player'})
teams = teams.rename(columns={'TEAM_NAME': 'Team'})

# Perform left joins
results_df = (boxscores
              .merge(players[['PLAYER_ID', 'Player']], 
                     on='PLAYER_ID', how='left')
              .merge(teams[['TEAM_ID', 'Team']], 
                     on='TEAM_ID', how='left')
              .sort_values(by=['GAME_ID', 'TEAM_ID'])
              .drop(columns=['PLAYER_ID', 'TEAM_ID']))

# Disconnect database connection
con.close()

# Review results of join
print(results_df)