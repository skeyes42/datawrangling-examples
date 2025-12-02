# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_24_ScatterPlot.R
# DATE 2025-10-27
# DESCRIPTION: 

library(ggplot2)
library(DBI)
library(RSQLite)
library(dplyr)
library(tidyr)

# Connect to database
path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Build query that will do join
query <- tbl(con, "Boxscores") |>
  left_join(tbl(con, "Players") |> rename(Player = PLAYER_NAME), by = "PLAYER_ID") |>
  left_join(tbl(con, "Teams") |> rename(Team = TEAM_NAME), by = "TEAM_ID") |>
  arrange(GAME_ID, TEAM_ID) |>
  select(-PLAYER_ID, -TEAM_ID)

# Run the query
results_df <- query |>
  collect()

# Create scatter plot
p <- ggplot(results_df, aes(x = FG3M, y = FGM, color = factor(Player))) +
  geom_point(size = 3) +
  labs(
    title = "Field Goals Made vs 3-Point Field Goals Made",
    x = "3-Point Field Goals Made (FG3M)",
    y = "Field Goals Made (FGM)",
    color = "Player ID"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold"),
    legend.position = "right"
  )

  print(p)