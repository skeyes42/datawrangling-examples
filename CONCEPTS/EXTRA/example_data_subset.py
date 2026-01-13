import pandas as pd

# Define the DataFrame using vectors of literal data
df = pd.DataFrame([
    {'GAME_ID': 1000, 'TEAM_ID': 100, 'PLAYER_ID': 1, 'FGM': 10, 'FG3M': 12, 'FTM': 12},
    {'GAME_ID': 1000, 'TEAM_ID': 100, 'PLAYER_ID': 2, 'FGM':  4, 'FG3M':  4, 'FTM':  7},
    {'GAME_ID': 1000, 'TEAM_ID': 200, 'PLAYER_ID': 3, 'FGM':  2, 'FG3M':  6, 'FTM':  5},
    {'GAME_ID': 1000, 'TEAM_ID': 200, 'PLAYER_ID': 4, 'FGM':  8, 'FG3M':  2, 'FTM':  7},
    {'GAME_ID': 2000, 'TEAM_ID': 100, 'PLAYER_ID': 1, 'FGM': 10, 'FG3M':  4, 'FTM': 10},
    {'GAME_ID': 2000, 'TEAM_ID': 100, 'PLAYER_ID': 2, 'FGM': 11, 'FG3M':  5, 'FTM':  4},
    {'GAME_ID': 2000, 'TEAM_ID': 300, 'PLAYER_ID': 5, 'FGM':  8, 'FG3M': 10, 'FTM':  9},
    {'GAME_ID': 2000, 'TEAM_ID': 300, 'PLAYER_ID': 6, 'FGM':  7, 'FG3M':  6, 'FTM':  3},
])

print(df)