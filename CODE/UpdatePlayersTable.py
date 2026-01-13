# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: UpdatePlayersTable.py
# DATE 2025-10-19
# DESCRIPTION: 
# This Python program connects to an SQLite database and performs a data 
# modification operation, specifically updating a player's name within 
# the Players table. It demonstrates how to execute SQL commands that 
# alter data stored in a database file.

import os
import sqlite3
import pandas as pd

# Connect to a database
# Use a context manager to handle the connection automatically
path_to_database = os.path.join(os.getenv("EXAMPLES", ""), "Boxscores.db")
with sqlite3.connect(path_to_database) as con:
    
    # Create a cursor object
    cur = con.cursor()
    
    # Construct the SQL UPDATE statement
    sql_update_query = (
        "UPDATE Players "
        "SET PLAYER_NAME = 'Johnie' "
        "WHERE PLAYER_ID = 2;"
    )
    
    # Execute the statement
    cur.execute(sql_update_query)
    
    # Commit the changes to the database
    con.commit()
    
    # Verify the table was written by reading it back
    # Using pandas is a common and convenient way to read SQL 
    # data into a DataFrame
    results_df = pd.read_sql_query("SELECT * FROM Players", con)
    print(results_df)

print("Done")
