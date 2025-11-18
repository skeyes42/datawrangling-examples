# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_12_BuildPlayersObject.py
# DATE 2025-10-20
# DESCRIPTION: 

import sqlite3
import pandas as pd
import os
from dataclasses import dataclass
from typing import Protocol

# Define the class
@dataclass
class Players:
    path: str
    
    def players_dataframe(self) -> pd.DataFrame:
        
        # Connect to the database
        con = sqlite3.connect(self.path)
        
        try:
            # Query the Players table
            query = "SELECT * FROM Players"
            results_df = pd.read_sql_query(query, con)
            
        finally:
            # Always close the connection
            con.close()
        
        return results_df


def get_Players_instance(db_path: str) -> Players:
    return Players(path=db_path)


if __name__ == "__main__":
    # Set path to Players database
    path_to_database = os.path.join(os.getenv("EXAMPLES", ""), "Boxscores.db")
    
    # Instantiate the Players class
    players_object = get_Players_instance(path_to_database)
    
    # Call the players_dataframe() method to get the data
    players_data = players_object.players_dataframe()
    
    # Display the resulting data frame
    print(players_data)
    
    print('Done')
