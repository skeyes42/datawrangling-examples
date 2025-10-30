# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_5_SimpleJoinBoxscores.py
# DATE 2025-10-19
# DESCRIPTION: 

import os
import sqlite3
import pandas as pd

# Connect to database
path_to_database = os.path.join(os.getenv("EXAMPLES", ""), "Boxscores.db")

try:
    with sqlite3.connect(path_to_database) as con:
        # Build the query using pandas
        
        # Read tables into DataFrames
        boxscores_df = pd.read_sql("SELECT * FROM Boxscores", con)
        players_df = pd.read_sql("SELECT * FROM Players", con)
        teams_df = pd.read_sql("SELECT * FROM Teams", con)

        # Perform left joins
        # The `on` parameter specifies the common column, and `how='left'` specifies a left join
        query_df = boxscores_df.merge(
            players_df.rename(columns={'PLAYER_NAME': 'Player'}), 
            on='PLAYER_ID', 
            how='left'
        )

        query_df = query_df.merge(
            teams_df.rename(columns={'TEAM_NAME': 'Team'}), 
            on='TEAM_ID', 
            how='left'
        )

        # Apply filtering, sorting, and selecting columns
        # `.iloc[1:]` is the pandas equivalent of `row_number() > 1`
        results_df = (
            query_df.iloc[1:]
            .sort_values(by=['GAME_ID', 'TEAM_ID'])
            .drop(columns=['PLAYER_ID', 'TEAM_ID'])
        )

        # Display the results (equivalent to show_query and View)
        # In pandas, the `.to_sql()` method is used to write to a database.
        print("Final DataFrame structure (equivalent to show_query):")
        print(results_df.head())

        # 4. Review results of join
        print("\nDisplaying all results (equivalent to View):")
        print(results_df)

except sqlite3.Error as e:
    print(f"Database error: {e}")
except FileNotFoundError:
    print(f"Error: The database file was not found at {path_to_database}.")

# The database connection is automatically closed by the `with` statement.
