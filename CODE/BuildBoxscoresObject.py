# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_11_BuildBoxscoresObject.py
# DATE 2025-10-20
# DESCRIPTION: 

import sqlite3
import pandas as pd
import os

# Define the class
class Boxscores:
    
    def __init__(self, path_to_database=""):
        self.path = path_to_database
    
    def boxscores_dataframe(self):
        # Connect to database
        con = sqlite3.connect(self.path)
        
        try:
            # Read tables
            boxscores = pd.read_sql_query("SELECT * FROM Boxscores", con)
            players = pd.read_sql_query("SELECT * FROM Players", con)
            teams = pd.read_sql_query("SELECT * FROM Teams", con)
            
            # Perform left joins
            results_df = boxscores.merge(players, on='PLAYER_ID', how='left')
            results_df = results_df.merge(teams, on='TEAM_ID', how='left')
            
            # Drop PLAYER_ID and TEAM_ID columns
            results_df = results_df.drop(columns=['PLAYER_ID', 'TEAM_ID'])
            
            return results_df
            
        finally:
            # Always close the connection
            con.close()


def get_boxscores_instance(db_path):
    return Boxscores(path_to_database=db_path)


if __name__ == "__main__":
    # Set path to Boxscores database
    path_to_database = os.path.join(os.getenv("EXAMPLES", ""), "Boxscores.db")
    
    # Instantiate the Boxscores class
    boxscores_object = get_boxscores_instance(path_to_database)
    
    # Call the boxscores_dataframe() method to get the data
    boxscores_data = boxscores_object.boxscores_dataframe()
    
    # Display the resulting dataframe
    print(boxscores_data)
    
    print('Done')
