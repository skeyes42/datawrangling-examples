# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_3_WriteBoxscoresTable.py
# DATE 2025-10-13
# DESCRIPTION: Overwrite Players table

import os
import sqlite3
import pandas as pd
from io import StringIO

# The path to the database will be dependent on your environment.
# Using os.getenv for environment variables is a good practice.
# For this example, a simple filename is used.
path_to_database = os.path.join(os.getenv("EXAMPLES", ""), "Boxscores.db")

# Connect to a database.
# The `with` statement ensures the connection is properly closed.

with sqlite3.connect(path_to_database) as conn:
    
    # 2. Create a dataframe of Players data from a CSV string.
    csv_players_data = """PLAYER_ID,PLAYER_NAME
1,Fred
2,John
3,Trevor
4,Alex
5,Jim
6,Steve
7,Herb"""

    players_data_df = pd.read_csv(StringIO(csv_players_data), dtype={'PLAYER_ID': int, 'PLAYER_NAME': str})

    # Write the data frame to a database table.
    # The `to_sql()` function creates or overwrites the "Players" table.
    # `index=False` prevents writing the DataFrame's index as a column.
    players_data_df.to_sql("Players", conn, if_exists="replace", index=False)

    # Verify the table was written by reading it back into a DataFrame.
    results_df = pd.read_sql_query("SELECT * FROM Players", conn)

    # Print the DataFrame to view the results.
    print("Contents of the 'Players' table:")
    print(results_df)

# The connection is automatically closed by the `with` statement.

print('Done')

