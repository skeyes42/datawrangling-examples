# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_1_LoadBoxscoresTable.py
# DATE 2025-10-19
# DESCRIPTION: 

import os
import pandas as pd
import sqlite3

# Define file paths
path_to_data = os.getenv("EXAMPLES")
path_to_database = os.path.join(path_to_data, "boxscores.db")
path_to_csv = os.path.join(path_to_data, "boxscores.csv")

# Connect to the SQLite database
# Using a context manager (`with...`) ensures the connection is 
# automatically closed
with sqlite3.connect(path_to_database) as db_connection:
    # Read the CSV file into a pandas DataFrame
    df_boxscores = pd.read_csv(path_to_csv)

    # Append the data from the DataFrame to the "Boxscores" table 
    # in the database. The `if_exists` parameter handles what to 
    # do if the table already exists. index=False prevents pandas 
    # from writing the DataFrame index as a column.
    df_boxscores.to_sql("Boxscores", db_connection, if_exists='replace', 
                        index=False)

# In Python, you can print the DataFrame head or use a more advanced 
# data viewer.
print(df_boxscores.head())

print("Done")

