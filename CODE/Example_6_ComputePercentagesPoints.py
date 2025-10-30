# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_6_ComputePercentagesPoints.py
# DATE 2025-10-19
# DESCRIPTION: 

import os
import sqlite3
import pandas as pd
import numpy as np

# Connect to database
# The equivalent of Sys.getenv() is os.getenv() in Python.
path_to_database = os.path.join(os.getenv("EXAMPLES", ""), "Boxscores.db")

# Create a connection using the built-in sqlite3 library.
con = sqlite3.connect(path_to_database)

# Read the data into a pandas DataFrame
results_df = pd.read_sql_query("SELECT * FROM Boxscores", con)

# Perform data transformations with pandas
results_df = (
    results_df.assign(
        # Convert columns to float type for calculations.
        FGM=results_df['FGM'].astype(float),
        FGA=results_df['FGA'].astype(float),
        FG3M=results_df['FG3M'].astype(float),
        FG3A=results_df['FG3A'].astype(float),
        FTM=results_df['FTM'].astype(float),
        FTA=results_df['FTA'].astype(float),
    )
    .assign(
        # Create the percentage columns using numpy.where to handle division by zero.
        FG_PCT=np.where(results_df['FGA'] == 0, 0, (results_df['FGM'] / results_df['FGA']) * 100),
        FG3_PCT=np.where(results_df['FG3A'] == 0, 0, (results_df['FG3M'] / results_df['FG3A']) * 100),
        FT_PCT=np.where(results_df['FTA'] == 0, 0, (results_df['FTM'] / results_df['FTA']) * 100),
    )
    .assign(
        # Calculate points
        FG2_PTS=(results_df['FGM'] - results_df['FG3M']) * 2,
        FG3_PTS=results_df['FG3M'] * 3,
        FT_PTS=results_df['FTM'] * 1,
    )
    .assign(
        # Sum all the different types of points for the total score.
        PTS=lambda df: df['FG2_PTS'] + df['FG3_PTS'] + df['FT_PTS'],
    )
    # Arrange by GAME_ID, TEAM_ID
    .sort_values(['GAME_ID', 'TEAM_ID'])
    # Select columns by dropping the temporary ones
    .drop(columns=['FG2_PTS', 'FG3_PTS', 'FT_PTS'])
)

# Show the query plan (conceptual equivalent)
print("Query operations completed in pandas DataFrame.")

# Put the new data back into the database: overwrite the Boxscores table
# Use pandas `to_sql()` method to write the DataFrame to the database.
results_df.to_sql(
    "Boxscores",
    con,
    if_exists="replace",
    index=False
)

# Write the new dataframe to a CSV file.
results_df.to_csv("results.csv", index=False)

# Disconnect database connection
con.close()

# Review results of join
print("\nFirst 5 rows of the modified DataFrame:")
print(results_df.head())
