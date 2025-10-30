# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_23_PlotLineChart.R
# DATE 2025-10-26
# DESCRIPTION: 

library(ggplot2)
library(dplyr)
library(tidyr)
library(readr)
library(RSQLite)

# Connect to database
path_to_database <- paste0(Sys.getenv("EXAMPLES"), "Boxscores.db")
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Build query that will do join
query <- tbl(con, "Boxscores") |>
  left_join(tbl(con, "Players") |> rename(Player = PLAYER_NAME), by = "PLAYER_ID") |>
  left_join(tbl(con, "Teams") |> rename(Team = TEAM_NAME), by = "TEAM_ID") |>
  filter(Player == "John") |>
  arrange(GAME_ID, TEAM_ID) |>
  select(-PLAYER_ID, -TEAM_ID)

# Run the query
results_df <- query |>
  collect()

# Select and filter the data for a specific player (e.g., Player 1)
player1_stats <- results_df |>
  select(GAME_ID, FGM, FG3M, FTM)

# Reshape the data from wide to long format
player1_long <- player1_stats |>
  pivot_longer(cols = c(FGM, FG3M, FTM),
               names_to = "statistic",
               values_to = "value")

# Ensure GAME_ID is treated as a continuous numeric variable
player1_long$GAME_ID <- as.numeric(player1_long$GAME_ID)

# Create the line plot with corrected syntax
p <- ggplot(player1_long, aes(x = GAME_ID, y = value, color = statistic)) +
  geom_line(aes(group = statistic), linewidth = 1.2) +
  geom_point(size = 3) +
  labs(
    title = "John's Scoring Statistics Over Time",
    subtitle = "Comparing Field Goals, 3-Pointers, and Free Throws Made",
    x = "Game ID",
    y = "Count",
    color = "Statistic"
  ) +
  theme_minimal() + # Use a clean, minimal theme
  scale_color_brewer(palette = "Set1")

# Print the plot
print(p)

# Clean up database connection
dbDisconnect(con)
