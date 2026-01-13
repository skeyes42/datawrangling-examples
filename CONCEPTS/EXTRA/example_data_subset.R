# Define dataframe using literal vectors

df <- tibble::tribble(
  ~GAME_ID, ~TEAM_ID, ~PLAYER_ID, ~FGM, ~FG3M, ~FTM,
      1000,      100,          1,   10,    12,   12,
      1000,      100,          2,    4,     4,    7,
      1000,      200,          3,    2,     6,    5,
      1000,      200,          4,    8,     2,    7,
      2000,      100,          1,   10,     4,   10,
      2000,      100,          2,   11,     5,    4,
      2000,      300,          5,    8,    10,    9,
      2000,      300,          6,    7,     6,    3
)


# Display the dataframe
print(df)

# Different subset: boxscores has TEAM_ID = 400 which is not found in PLAYERs table
# Different subset: PLAYER has extra player not found in PLAYERs table

# Add a player with no boxscore data
players_df <- data.frame(
  PLAYER_ID = c(1, 2, 3, 4, 5, 6, 7),  # Added player 7
  PLAYER_NAME = c("Fred", "John", "Trevor", "Alex", "Jim", "Steve", "Michael")
)

# Add a boxscore with no player data
boxscores_df <- rbind(boxscores_df, 
                      data.frame(GAME_ID = 3000, TEAM_ID = 400, PLAYER_ID = 99, 
                                 FGM = 15, FG3M = 3, FTM = 8))