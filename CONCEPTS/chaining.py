import pandas as pd

# Define the DataFrame using vectors of literal data
df = pd.DataFrame({
    'GAME_ID': [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000],
    'TEAM_ID': [100, 100, 200, 200, 100, 100, 300, 300],
    'PLAYER_ID': [1, 2, 3, 4, 1, 2, 5, 6],
    'FGM': [10, 4, 2, 8, 10, 11, 8, 7],
    'FG3M': [12, 4, 6, 2, 4, 5, 10, 6],
    'FTM': [12, 7, 5, 7, 10, 4, 9, 3]
})


# Apply transformations using method chaining
df = (df
      .assign(SCORING_EFFORT=lambda x: x['FGM'] + x['FG3M'] + x['FTM'])
      .query('SCORING_EFFORT > 19')
     )

print(df)

df1 = df

# An alternative way to express the above.
df1 = df1.assign(SCORING_EFFORT=
    lambda x: x['FGM'] + x['FG3M'] + x['FTM']).query('SCORING_EFFORT > 19')

print(df1)