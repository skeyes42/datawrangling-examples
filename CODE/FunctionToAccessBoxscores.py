# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_9_FunctionToAccessBoxscores.py
# DATE 2025-10-20
# DESCRIPTION: 

import sqlite3
import pandas as pd
import os

# Define the function
def get_boxscores(path_to_database):
    
    # Connect to database
    con = sqlite3.connect(path_to_database)
    
    try:
        # Query to select all columns from Boxscores table
        query = "SELECT * FROM Boxscores"
        
        # Read data into pandas DataFrame
        results_df = pd.read_sql_query(query, con)
        
        return results_df
    
    finally:
        # Ensure connection is closed even if error occurs
        con.close()

# Main execution
if __name__ == "__main__":
    # Get path to database from environment variable
    examples_path = os.getenv("EXAMPLES")
    path_to_database = os.path.join(examples_path, "Boxscores.db")
    
    # Get boxscores data
    df = get_boxscores(path_to_database)
    
    # Display the DataFrame
    print(df)
    
    print("Done")