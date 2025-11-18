# FILE: Example_2_RetrieveBoxscoresTable.py
# DATE 2025-10-19
# DESCRIPTION: Retrieves all rows from the Boxscores table in a SQLite database.

import sqlite3
import pandas as pd
import os

# Connect to database
path_to_database = os.path.join(os.getenv("EXAMPLES"), "Boxscores.db")

# Use a context manager (the 'with' statement) to handle the connection.
# This ensures the connection is automatically closed, even if errors occur.
try:
    with sqlite3.connect(path_to_database) as con:
        # The pandas read_sql function executes the SQL query and 
        # returns a DataFrame.
        query_text = "SELECT * FROM Boxscores"
        print(f"Executing query: {query_text}")

        results_df = pd.read_sql(query_text, con)

    print('-------------------------')
    print(results_df)
    print("Done")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

