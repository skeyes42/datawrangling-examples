import pandas as pd

df = pd.DataFrame({
    'GAME_ID': [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000],
    'TEAM_ID': [100, 100, 200, 200, 100, 100, 300, 300],
    'PLAYER_ID': [1, 2, 3, 4, 1, 2, 5, 6],
    'FGM': [10, 4, 2, 8, 10, 11, 8, 7],
    'FG3M': [12, 4, 6, 2, 4, 5, 10, 6],
    'FTM': [12, 7, 5, 7, 10, 4, 9, 3]
})

result = (
    df
    .assign(TOTAL_PTS = lambda x: 2*x['FGM'] + 3*x['FG3M'] + x['FTM'])
    .groupby(['GAME_ID', 'TEAM_ID'], as_index=False)
    .agg(TEAM_PTS=('TOTAL_PTS', 'sum'))
    .sort_values(['GAME_ID', 'TEAM_PTS'], ascending=[True, False])
)

print(result)