# Define dataframe using literal vectors

df <- tibble::tribble(
  ~GAME_ID, ~TEAM_ID, ~PLAYER_ID, ~FGM, ~FG3M, ~FTM,
      1000L,      100L,          1L,   10L,    12L,   12L,
      1000L,      100L,          2L,    4L,     4L,    7L,
      1000L,      200L,          3L,    2L,     6L,    5L,
      1000L,      200L,          4L,    8L,     2L,    7L,
      2000L,      100L,          1L,   10L,     4L,   10L,
      2000L,      100L,          2L,   11L,     5L,    4L,
      2000L,      300L,          5L,    8L,    10L,    9L,
      2000L,      300L,          6L,    7L,     6L,    3L
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