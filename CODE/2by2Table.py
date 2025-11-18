# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_27_2by2Table.py
# DATE 2025-11-01
# DESCRIPTION: 

import pandas as pd
import sqlite3
import os

# Connect to database
path_to_database = os.path.join(
    os.environ.get("EXAMPLES", ""), "Boxscores.db")

con = sqlite3.connect(path_to_database)

# Get selected numeric variables from Boxscores table
query_sql = "SELECT FGM, FG3M FROM Boxscores"
results_df = pd.read_sql_query(query_sql, con)

# Disconnect
con.close()

# Convert numeric columns to 2x2 factor variables
processed_data = results_df.copy() 
processed_data['FG3M_category'] = pd.cut(
    processed_data['FG3M'], 
    bins=[-float('inf'), 2, float('inf')], 
    labels=['Low 3P', 'High 3P']
)
processed_data['FGM_category'] = pd.cut(
    processed_data['FGM'], 
    bins=[-float('inf'), 5, float('inf')], 
    labels=['Low FG', 'High FG']
)
# Ensure categories are ordered correctly
cat = processed_data['FG3M_category']
cat = cat.cat.reorder_categories(
    ['Low 3P', 'High 3P'], ordered=True)
processed_data['FG3M_category'] = cat

# Generate the 2x2 table using pandas.crosstab()
fg_table = pd.crosstab(
    processed_data['FG3M_category'], 
    processed_data['FGM_category'])

# Print the table
print(fg_table)
