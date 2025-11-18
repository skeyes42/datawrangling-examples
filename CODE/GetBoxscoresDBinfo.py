# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_0_GetBoxscoresDBinfo.py
# DATE 2025-10-19
# DESCRIPTION: 

import sqlite3
import os

# Get the database path from environment variable
path_to_database = os.path.join(os.environ.get("EXAMPLES", ""), "Boxscores.db")

# Establish a connection to the SQLite database
con = sqlite3.connect(path_to_database)

# Create a cursor object
cursor = con.cursor()

# Get table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = [row[0] for row in cursor.fetchall()]
print(table_names)

print('----------------------------------------------------------')

# Replace with the name of the table you want to inspect
table_name = "Boxscores"

# Execute the PRAGMA statement to get table info
cursor.execute(f"PRAGMA table_info({table_name});")
column_info = cursor.fetchall()

# Print the column information
# PRAGMA table_info returns: cid, name, type, notnull, dflt_value, pk

print("Column Information:")
for col in column_info:
    parts = [
    f"ID: {col[0]}",
    f"Name: {col[1]}",
    f"Type: {col[2]}",
    f"NotNull: {col[3]}",
    f"Default: {col[4]}",
    f"PK: {col[5]}",
]
    print(", ".join(parts))
    
# Close the connection
con.close()