import pandas as pd

boxscores = pd.DataFrame([
    # GAME_ID  TEAM_ID  PLAYER_ID  FGM 
    [1000,     100,     1,         10, ],
    [1000,     100,     2,          4, ],
    [1000,     200,     3,          2, ],
    [1000,     200,     4,          8, ],
    [2000,     100,     1,         10, ],
    [2000,     100,     2,         11, ],
    [2000,     300,     5,          8, ],
    [2000,     300,     6,          7, ],
    [3000,     200,     3,          5, ],
    [3000,     200,     4,          3, ],
    [3000,     300,     5,          4, ],
    [3000,     300,     6,          8, ],
], columns=['GAME_ID', 'TEAM_ID', 'PLAYER_ID', 'FGM'])

print("Original Boxscore Data:")
print(boxscores.to_markdown(index = False))

teammate_pairs = boxscores.merge(
    boxscores,
    on=['GAME_ID', 'TEAM_ID'],
    suffixes=('_p1', '_p2')
)

print(teammate_pairs.to_markdown(index = False))

# Avoid pairing a player with themselves
# Use < instead of != to avoid duplicate pairs (1,2) and (2,1)
teammate_pairs = teammate_pairs[
    teammate_pairs['PLAYER_ID_p1'] < teammate_pairs['PLAYER_ID_p2']
]

# teammate_pairs after filtering
print()


print("\n\nTeammate Pairs (via self-join):")
print(teammate_pairs[['GAME_ID', 'TEAM_ID', 'PLAYER_ID_p1', 'PLAYER_ID_p2',
                      'FGM_p1', 'FGM_p2']])
