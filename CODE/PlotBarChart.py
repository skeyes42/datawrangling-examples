# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: PlotBarChart.py
# DATE 2025-10-27
# DESCRIPTION: 
# This Python program is a specialized data visualization script designed 
# for player performance analysis. It extracts specific shooting statistics 
# for a player named "John" and generates a patterned bar chart to compare 
# different types of made shots across multiple games.

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import os

path_to_scripts = os.getenv("EXAMPLES")
path_to_database = os.path.join(os.getenv("EXAMPLES"), "Boxscores.db")

# Connect to database
con = sqlite3.connect(path_to_database)

# Build and execute query
query = """
SELECT b.*, p.PLAYER_NAME as Player, t.TEAM_NAME as Team
FROM Boxscores b
LEFT JOIN Players p ON b.PLAYER_ID = p.PLAYER_ID
LEFT JOIN Teams t ON b.TEAM_ID = t.TEAM_ID
WHERE p.PLAYER_NAME = 'John'
ORDER BY b.GAME_ID, b.TEAM_ID
"""

results_df = pd.read_sql_query(query, con)
results_df = results_df.drop(columns=['PLAYER_ID', 'TEAM_ID'])

# Reshape to long format
results_long_df = pd.melt(
    results_df,
    id_vars=[col for col in results_df.columns if col not in ['FGM', 'FG3M', 'FTM']],
    value_vars=['FGM', 'FG3M', 'FTM'],
    var_name='Stat_Type',
    value_name='Count'
)

results_long_df.to_csv("Results_Long.csv", index=False)

# Create grouped bar chart with patterns
fig, ax = plt.subplots(figsize=(10, 6))

# Define patterns (hatches) for each stat type
patterns = {'FGM': '///', 'FG3M': 'xxx', 'FTM': '...'}
colors = {'FGM': 'gray', 'FG3M': 'gray', 'FTM': 'gray'}

# Get unique games and stat types
games = results_long_df['GAME_ID'].unique()
stat_types = ['FGM', 'FG3M', 'FTM']
x = range(len(games))
width = 0.25

# Create bars for each stat type with different patterns
for i, stat in enumerate(stat_types):
    data = results_long_df[results_long_df['Stat_Type'] == stat]
    values = [data[data['GAME_ID'] == game]['Count'].values[0] if len(data[data['GAME_ID'] == game]) > 0 else 0 
              for game in games]
    
    bars = ax.bar([xi + i*width for xi in x], values, width, 
                   label=stat, 
                   color=colors[stat],
                   edgecolor='black',
                   hatch=patterns[stat])

ax.set_xlabel('Game ID')
ax.set_ylabel('Count')
ax.set_title('FGM, FG3M, and FTM by Game for John')
ax.set_xticks([xi + width for xi in x])
ax.set_xticklabels(games)
ax.legend(title='Statistic')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('bar_chart_patterns.png', dpi=300, bbox_inches='tight')
plt.show()

con.close()
print("Done")

