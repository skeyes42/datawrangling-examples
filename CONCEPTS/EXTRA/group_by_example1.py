import pandas as pd

# Create the dataframe
boxscores_df = pd.DataFrame({
    'GAME_ID': [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000],
    'TEAM_ID': [100, 100, 200, 200, 100, 100, 300, 300],
    'PLAYER_ID': [1, 2, 3, 4, 1, 2, 5, 6],
    'FGM': [10, 4, 2, 8, 10, 11, 8, 7],
    'FG3M': [12, 4, 6, 2, 4, 5, 10, 6],
    'FTM': [12, 7, 5, 7, 10, 4, 9, 3]
})

# Add points column
boxscores_df['PTS'] = boxscores_df['FGM'] * 2 + boxscores_df['FG3M'] * 3 + boxscores_df['FTM']

# Group by game
grouped_by_game = boxscores_df.groupby('GAME_ID')

print(f"Number of groups: {grouped_by_game.ngroups}")

# this statement is interesting, but a little hard to read
#print(f"Group keys: {' '.join(str(k) for k in grouped_by_game.groups.keys())}\n")
# this statment does the same thing:
print(f"Group keys: {list(grouped_by_game.groups.keys())}")
# Output: Group keys: [1000, 2000]

# Iterate through groups
for game_id, game_data in grouped_by_game:
    print(f"--- Game {game_id} ---")
    print(f"Players: {len(game_data)}")
    print(f"Total points: {game_data['PTS'].sum()}\n")

# Nested grouping: Game -> Team
grouped_nested = boxscores_df.groupby(['GAME_ID', 'TEAM_ID'])

print("=== Team Summaries by Game ===\n")

for (game_id, team_id), team_data in grouped_nested:
    print(f"Game {game_id}, Team {team_id}")
    print(f"  Players: {', '.join(str(p) for p in team_data['PLAYER_ID'])}")
    print(f"  Team points: {team_data['PTS'].sum()}")
    top_scorer_idx = team_data['PTS'].idxmax()
    print(f"  Top scorer: {team_data.loc[top_scorer_idx, 'PLAYER_ID']} "
          f"with {team_data['PTS'].max()} pts\n")

# Equivalent to group_walk for side effects
print("=== Using apply for side effects ===\n")

def print_game_avg(group):
    game_id = group['GAME_ID'].iloc[0]
    avg_pts = round(group['PTS'].mean(), 1)
    print(f"Game {game_id} - Avg points per player: {avg_pts}")
    return None  # returning None since we're just doing side effects

boxscores_df.groupby('GAME_ID').apply(print_game_avg, include_groups=True)