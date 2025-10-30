# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_23_PlotLineChart.py
# DATE 2025-10-26
# DESCRIPTION: 

import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt

# Get path to database
path_to_scripts = os.getenv("EXAMPLES")
path_to_database = os.path.join(path_to_scripts, "Boxscores.db")

# Connect to database
con = sqlite3.connect(path_to_database)

# Query the data
season_data = pd.read_sql_query("SELECT FG3_PCT_AVG, SEASON_WINS FROM Season2025", con)

# Close the database connection
con.close()

# Sort data by SEASON_WINS
season_data = season_data.sort_values('SEASON_WINS')

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(season_data['SEASON_WINS'], season_data['FG3_PCT_AVG'], 
         color='#1f77b4', linewidth=1.2, marker='o', markersize=8, alpha=0.7)

plt.title('3-Point Field Goal Percentage vs Season Wins', 
          fontsize=16, fontweight='bold')
plt.suptitle('2025 Season', y=0.96, fontsize=12, color='gray')
plt.xlabel('Season Wins', fontsize=12, fontweight='bold')
plt.ylabel('Average 3-Point FG %', fontsize=12, fontweight='bold')

plt.grid(True, which='major', alpha=0.3)
plt.grid(False, which='minor')
plt.style.use('seaborn-v0_8-whitegrid')

plt.tight_layout()
plt.show()