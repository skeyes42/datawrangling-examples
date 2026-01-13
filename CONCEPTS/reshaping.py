import pandas as pd
import sqlite3
import os

# Connect to database with error handling
db_path = os.path.join(os.getenv("EXAMPLES", ""), "Boxscores.db")
conn = sqlite3.connect(db_path)

# 1. Bring into Boxscores the player and team names via SQL (mimics the lazy join)
# Using SQL for the initial join is more memory-efficient, similar to dbplyr/tbl
query_sql = """
SELECT b.*, p.PLAYER_NAME, t.TEAM_NAME
FROM Boxscores b
LEFT JOIN Players p ON b.PLAYER_ID = p.PLAYER_ID
LEFT JOIN Teams t ON b.TEAM_ID = t.TEAM_ID
ORDER BY b.GAME_ID, b.TEAM_ID
"""

shooting = pd.read_sql_query(query_sql, conn)

# Drop ID columns to match the R select(-PLAYER_ID, -TEAM_ID)
shooting = shooting.drop(columns=['PLAYER_ID', 'TEAM_ID'])

print(shooting)
conn.close()

# 2. Pivot longer to stack all shot types
# Equivalent to pivot_longer
shooting_long = shooting.melt(
    id_vars=[col for col in shooting.columns 
        if col not in ['FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA']],
    value_vars=['FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA'],
    var_name='stat_type',
    value_name='count'
)

# 3. Calculate shooting percentages by player
# Extract 'shot_type' (FG, FG3, FT) and 'made_attempt' (M, A)
shooting_long['shot_type'] = shooting_long['stat_type'].str[:-1]
shooting_long['made_attempt'] = shooting_long['stat_type'].str[-1]

# Pivot wider to get 'M' and 'A' as columns
shooting_summary = shooting_long.pivot_table(
    index=['PLAYER_NAME', 'shot_type'],
    columns='made_attempt',
    values='count',
    aggfunc='sum'
).reset_index()

# Calculate percentages and summarize
shooting_summary['pct'] = (shooting_summary['M'] / 
                           shooting_summary['A']) * 100

# group_by and summarise
final_summary = shooting_summary.groupby(['PLAYER_NAME', 'shot_type']).agg(
    total_attempts=('A', 'sum'),
    shooting_pct=('pct', 'mean')
).reset_index()

print(final_summary)

