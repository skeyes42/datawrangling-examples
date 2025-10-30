# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_8_SummarizeTeamLevel.py
# DATE 2025-10-20
# DESCRIPTION: 

import os
import pandas as pd
import sqlite3

# Connect to the database
try:
    path_to_database = os.environ.get("EXAMPLES") + "Boxscores.db"
except TypeError:
    print("The 'EXAMPLES' environment variable is not set.")
    exit()

con = sqlite3.connect(path_to_database)

# Read the entire 'Boxscores' table into a pandas DataFrame.
boxscores_df = pd.read_sql("SELECT * FROM Boxscores", con)

# Replicate the dplyr query with pandas
query_results = boxscores_df.groupby(['TEAM_ID', 'GAME_ID']).agg(
    FG_PCT_AVG=('FG_PCT', 'mean'),
    FG3_PCT_AVG=('FG3_PCT', 'mean'),
    FT_PCT_AVG=('FT_PCT', 'mean'),
    GAME_WIN=('WIN_LOSS', 'max')
).reset_index()

query_results = query_results.groupby('TEAM_ID').agg(
    FG_PCT_AVG=('FG_PCT_AVG', 'mean'),
    FG3_PCT_AVG=('FG3_PCT_AVG', 'mean'),
    FT_PCT_AVG=('FT_PCT_AVG', 'mean'),
    SEASON_WINS=('GAME_WIN', 'sum')
).reset_index()


# Add a new table to Boxscores.db
# The `to_sql` method writes a DataFrame to a database table.
query_results.to_sql(
    "Season2025", 
    con, 
    if_exists='replace', 
    index=False
)

print(query_results)

# Disconnect database connection
con.close()

print("Done")
