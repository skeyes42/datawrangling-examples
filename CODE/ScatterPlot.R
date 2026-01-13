# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: ScatterPlot.R
# DATE 2025-10-27
# DESCRIPTION: 
# This R program performs an end-to-end data analysis workflow: it connects 
# to a database, performs complex table joins using dbplyr, and creates a 
# professional visualization using ggplot2.

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

# Create scatter plot with different shapes
p <- ggplot(results_df, aes(x = FG3M, y = FGM, shape = factor(Player))) +
  geom_point(size = 3, fill = "gray50", color = "black") +
  scale_shape_manual(values = c(21, 22, 23, 24, 25, 8)) +
  labs(
    title = "Field Goals Made vs 3-Point Field Goals Made",
    x = "3-Point Field Goals Made (FG3M)",
    y = "Field Goals Made (FGM)",
    shape = "Player ID"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold"),
    legend.position = "right"
  )

  print(p)