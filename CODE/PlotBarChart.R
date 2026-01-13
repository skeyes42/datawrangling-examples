# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: PlotBarChart.R
# DATE 2025-10-27
# DESCRIPTION: 
# This R program connects to a sports database to extract, process, and 
# visualize the performance statistics of a specific player named "John."

library(tidyverse)
library(RSQLite)
library(DBI)
library(dplyr)
library(readr)
library(ggplot2)
library(ggpattern)

path_to_scripts <- Sys.getenv("EXAMPLES")

# Connect to database
path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Build query that will do join
query <- tbl(con, "Boxscores")    |>
  left_join(tbl(con, "Players")   |> rename(Player = PLAYER_NAME), by = "PLAYER_ID") |>
    left_join(tbl(con, "Teams")   |> rename(Team = TEAM_NAME),     by = "TEAM_ID")   |>
      filter(Player == "John")    |>
        arrange(GAME_ID, TEAM_ID) |>
          select(-PLAYER_ID, -TEAM_ID)
   
# Run the query
results_df <- query |>
  collect()

# Reshape the data from wide to long format
# This is necessary for ggplot2 to create a grouped bar chart
results_long_df <- results_df |>
  pivot_longer(
    cols = c(FGM, FG3M, FTM),  # Columns to pivot
    names_to = "Stat_Type",     # New column for the variable names
    values_to = "Count"         # New column for the values
  ) |> write_csv("Results_Long.csv")
    




p <- ggplot(results_long_df, aes(x = factor(GAME_ID), y = Count, fill = Stat_Type)) +
  geom_bar_pattern(
    aes(pattern = Stat_Type),
    stat = "identity", 
    position = "dodge",
    fill = "gray70",
    pattern_fill = "black",
    pattern_density = 0.1,
    pattern_spacing = 0.025
  ) +
  scale_pattern_manual(values = c("FGM" = "stripe", "FG3M" = "crosshatch", "FTM" = "circle")) +
  labs(
    title = "FGM, FG3M, and FTM by Game for John",
    x = "Game ID",
    y = "Count",
    pattern = "Statistic"
  ) +
  theme_minimal()

print(p)

# Disconnect
dbDisconnect(con)

print("Done")