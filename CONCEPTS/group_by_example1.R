library(dplyr)

# Create the dataframe
boxscores_df <- data.frame(
  GAME_ID = c(1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000),
  TEAM_ID = c(100, 100, 200, 200, 100, 100, 300, 300),
  PLAYER_ID = c(1, 2, 3, 4, 1, 2, 5, 6),
  FGM = c(10, 4, 2, 8, 10, 11, 8, 7),
  FG3M = c(12, 4, 6, 2, 4, 5, 10, 6),
  FTM = c(12, 7, 5, 7, 10, 4, 9, 3)
)

# Add points column
boxscores_df <- boxscores_df |>
  mutate(PTS = FGM * 2 + FG3M * 3 + FTM)

# Group by game
grouped_by_game <- boxscores_df |> group_by(GAME_ID)

cat("Number of groups:", n_groups(grouped_by_game), "\n")
cat("Group keys:", group_keys(grouped_by_game)$GAME_ID, "\n\n")

# Iterate through groups using group_split and group_keys
keys <- group_keys(grouped_by_game)
splits <- group_split(grouped_by_game)

for (i in seq_along(splits)) {
  game_id <- keys$GAME_ID[i]
  game_data <- splits[[i]]
  cat("--- Game", game_id, "---\n")
  cat("Players:", nrow(game_data), "\n")
  cat("Total points:", sum(game_data$PTS), "\n\n")
}

# Nested grouping: Game -> Team
grouped_nested <- boxscores_df |> group_by(GAME_ID, TEAM_ID)

cat("=== Team Summaries by Game ===\n\n")
keys <- group_keys(grouped_nested)
splits <- group_split(grouped_nested)

for (i in seq_along(splits)) {
  game_id <- keys$GAME_ID[i]
  team_id <- keys$TEAM_ID[i]
  team_data <- splits[[i]]
  
  cat(sprintf("Game %d, Team %d\n", game_id, team_id))
  cat("  Players:", paste(team_data$PLAYER_ID, collapse = ", "), "\n")
  cat("  Team points:", sum(team_data$PTS), "\n")
  cat("  Top scorer:", team_data$PLAYER_ID[which.max(team_data$PTS)], 
      "with", max(team_data$PTS), "pts\n\n")
}

# Using group_walk for side effects (like printing)
cat("=== Using group_walk ===\n\n")
boxscores_df |>
  group_by(GAME_ID) |>
  group_walk(~ {
    cat("Game", .y$GAME_ID, "- Avg points per player:", 
        round(mean(.x$PTS), 1), "\n")
  })