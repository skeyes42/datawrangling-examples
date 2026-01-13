# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: BuildTeamsObject.py
# DATE 2025-10-20
# DESCRIPTION: 
# This Python program is a data utility designed to extract 
# information specifically from the Teams table within a SQLite 
# database. It is structured to be modular, using modern Python 
# features to ensure the code is readable and maintainable.

import sqlite3
import pandas as pd
import os
from dataclasses import dataclass

# Define the class
@dataclass
class Teams:
  
    path: str
    
    def __init__(self, path_to_database: str = ""):
       
        self.path = path_to_database
    
    def teams_dataframe(self) -> pd.DataFrame:
       
        # Connect to database
        con = sqlite3.connect(self.path)
        
        try:
            # Query the Teams table
            query = "SELECT * FROM Teams"
            results_df = pd.read_sql_query(query, con)
            
            return results_df
        
        finally:
            # Always close the connection
            con.close()


def get_Teams_instance(db_path: str) -> Teams:
    return Teams(path_to_database=db_path)


if __name__ == "__main__":
    # Set path to Teams database
    path_to_database = os.path.join(os.getenv("EXAMPLES", ""), "Boxscores.db")
    
    # Instantiate the Teams class
    teams_object = get_Teams_instance(path_to_database)
    
    # Call the teams_dataframe() method to get the data
    teams_data = teams_object.teams_dataframe()
    
    # Display the resulting DataFrame
    print(teams_data)
    
    print('Done')