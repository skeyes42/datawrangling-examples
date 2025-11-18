# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_27_Correlation.py
# DATE 2025-11-04
# DESCRIPTION: 

import pandas as pd
import sqlite3
import os

# Connect to database
path_to_database = os.environ.get("EXAMPLES") + "Boxscores.db"
conn = sqlite3.connect(path_to_database)

# Get selected variables from the Boxscores table and load into a 
# pandas DataFrame
query = "SELECT * FROM Boxscores"
results_df = pd.read_sql_query(query, conn)

# Disconnect
conn.close()

# Drop the columns that were excluded in the R code's select statement
results_df = results_df.drop(
    columns=['GAME_ID', 'PLAYER_ID', 'TEAM_ID'], 
    errors='ignore')

# Calculate the correlation matrix for only the numeric columns
correlation_matrix = results_df.corr(numeric_only=True)

# View the result
print(correlation_matrix)
