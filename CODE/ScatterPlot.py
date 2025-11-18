# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_24_ScatterPlot.py
# DATE 2025-10-27
# DESCRIPTION: 

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Connect to database
path_to_database = os.path.join(os.environ.get("EXAMPLES", ""), "Boxscores.db")
con = sqlite3.connect(path_to_database)

# Build and execute query with joins
query = """
SELECT 
    b.*,
    p.PLAYER_NAME as Player,
    t.TEAM_NAME as Team
FROM Boxscores b
LEFT JOIN Players p ON b.PLAYER_ID = p.PLAYER_ID
LEFT JOIN Teams t ON b.TEAM_ID = t.TEAM_ID
ORDER BY b.GAME_ID, b.TEAM_ID
"""

# Execute query and load into DataFrame
results_df = pd.read_sql_query(query, con)

# Drop PLAYER_ID and TEAM_ID columns
results_df = results_df.drop(columns=['PLAYER_ID', 'TEAM_ID'])

# Close database connection
con.close()

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=results_df,
    x='FG3M',
    y='FGM',
    hue='Player',
    s=100,
    alpha=0.7
)

plt.title('Field Goals Made vs 3-Point Field Goals Made', 
          fontsize=14, fontweight='bold')
plt.xlabel('3-Point Field Goals Made (FG3M)', fontsize=12)
plt.ylabel('Field Goals Made (FGM)', fontsize=12)
plt.legend(title='Player ID', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()