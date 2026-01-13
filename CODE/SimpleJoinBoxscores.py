# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: SimpleJoinBoxscores.py
# DATE 2025-10-19
# DESCRIPTION: 
# This Python program retrieves and integrates basketball data 
# from an SQLite database using the pandas library. It follows 
# a classic data science pipeline: connecting to a source, 
# extracting raw tables, cleaning and merging them into a 
# human-readable format, and finally sorting and refining the 
# output.

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