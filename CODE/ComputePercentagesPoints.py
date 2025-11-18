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
    # The next .assign() block should use a lambda function to access 
    # the intermediate dataframe which has the newly converted float columns.
    .assign( 
        # Create the percentage columns using numpy.where to handle division 
        # by zero.
        FG_PCT=lambda df: np.where(df['FGA'] == 0, 
                                   0, 
                                   (df['FGM'] / df['FGA']) * 100),
        FG3_PCT=lambda df: np.where(df['FG3A'] == 0, 
                                    0, 
                                    (df['FG3M'] / df['FG3A']) * 100),
        FT_PCT=lambda df: np.where(df['FTA'] == 0, 
                                   0, 
                                   (df['FTM'] / df['FTA']) * 100),
    )
    .assign(
        # Calculate points (referencing the intermediate DataFrame using lambda/df)
        FG2_PTS=lambda df: (df['FGM'] - df['FG3M']) * 2,
        FG3_PTS=lambda df: df['FG3M'] * 3,
        FT_PTS=lambda df: df['FTM'] * 1,
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
