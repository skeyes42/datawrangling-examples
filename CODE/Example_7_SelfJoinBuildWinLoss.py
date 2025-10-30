
# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_7_SelfJoinBuildWinLoss.py
# DATE 2025-10-19
# DESCRIPTION: Corrected Python script to calculate Win/Loss records.

import sqlite3
import pandas as pd
import os

# Connect to database
path_to_database = os.getenv("EXAMPLES", "") + "Boxscores.db"
con = sqlite3.connect(path_to_database)

# Create scores by summarizing Boxscores
# This step is not actually needed since the subsequent query does the same thing.
# Keeping for demonstration but will replace its usage.
scores_df = pd.read_sql_query("SELECT GAME_ID, TEAM_ID, SUM(PTS) AS SCORE FROM Boxscores GROUP BY GAME_ID, TEAM_ID", con)

# Use a standard SQL query to perform the self-join and conditional logic.
# This query is already correct and creates the final results_df.
query_sql = """
    WITH scores AS (
        SELECT GAME_ID, TEAM_ID, SUM(PTS) AS SCORE
        FROM Boxscores
        GROUP BY GAME_ID, TEAM_ID
    )
    SELECT
        t1.GAME_ID,
        t1.TEAM_ID AS TEAM_ID,
        t1.SCORE AS SCORE,
        CASE
            WHEN t1.SCORE > t2.SCORE THEN 1
            WHEN t1.SCORE < t2.SCORE THEN 0
            ELSE NULL
        END AS WIN_LOSS
    FROM scores AS t1
    LEFT JOIN scores AS t2
        ON t1.GAME_ID = t2.GAME_ID
    WHERE t1.TEAM_ID != t2.TEAM_ID;
"""

# Execute the query and load results into a DataFrame
results_df = pd.read_sql_query(query_sql, con)

# Write results to a CSV file
results_df.to_csv("winloss.csv", index=False)

# Join results back to original boxscores and write to database
boxscores_df = pd.read_sql_query("SELECT * FROM Boxscores", con)

# Perform the left join using pandas
# The 'SCORE' column from results_df will be added to the boxscores_df
joined_df = pd.merge(boxscores_df, results_df, on=['GAME_ID', 'TEAM_ID'], how='left')

# Write the new data back into the Boxscores table, overwriting it
joined_df.to_sql(name='Boxscores', con=con, if_exists='replace', index=False)

# Disconnect database connection
con.close()

print(joined_df)