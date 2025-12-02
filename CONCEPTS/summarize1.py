import pandas as pd

df = pd.DataFrame({
    'GAME_ID': [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000],
    'TEAM_ID': [100, 100, 200, 200, 100, 100, 300, 300],
    'PLAYER_ID': [1, 2, 3, 4, 1, 2, 5, 6],
    'FGM': [10, 4, 2, 8, 10, 11, 8, 7],
    'FG3M': [12, 4, 6, 2, 4, 5, 10, 6],
    'FTM': [12, 7, 5, 7, 10, 4, 9, 3]
})

print("Original data:")
print(df)

# Summary by TEAM_ID
team_summary = (df
    .groupby('TEAM_ID', as_index=False)
    .agg(
        avg_fgm=('FGM', 'mean'),
        total_fgm=('FGM', 'sum'),
        n_players=('PLAYER_ID', 'count')
    )
)

print("\nSummary by team:")
print(team_summary)

# Summary by GAME_ID
game_summary = (df
    .groupby('GAME_ID', as_index=False)
    .agg(
        avg_fgm=('FGM', 'mean'),
        total_fgm=('FGM', 'sum')
    )
)

print("\nSummary by game:")
print(game_summary)

# Multiple grouping levels: GAME_ID and TEAM_ID
game_team_summary = (df
    .groupby(['GAME_ID', 'TEAM_ID'], as_index=False)
    .agg(
        avg_fgm=('FGM', 'mean'),
        total_fgm=('FGM', 'sum')
    )
)

print("\nSummary by game and team:")
print(game_team_summary)

"""
    Claude's comments about this program's R counterpart:
    The mutate + slice(1) pattern in R — Your R code uses mutate() 
    to add summary columns to all rows, then slice(1) to grab just 
    the first row per group. In pandas, groupby().agg() directly 
    produces one row per group, which is cleaner and more idiomatic.
    as_index=False — This keeps the grouping columns as regular columns 
    rather than making them the index, which mirrors R's ungroup() behavior.
    Named aggregation syntax — The agg(new_name=('column', 'function')) 
    syntax lets you rename columns in the same step, similar to how dplyr's 
    mutate() lets you name new columns inline.
"""