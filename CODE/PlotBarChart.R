# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_22_PlotBarChart.R
# DATE 2025-10-27
# DESCRIPTION: 

library(tidyverse)
library(RSQLite)
library(DBI)
library(dplyr)
library(readr)

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
  )

# Create the grouped bar chart
p <- ggplot(results_long_df, aes(x = factor(GAME_ID), y = Count, fill = Stat_Type)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(
    title = "FGM, FG3M, and FTM by Game for John",
    x = "Game ID",
    y = "Count",
    fill = "Statistic"
  ) +
  scale_fill_manual(values = c("FGM" = "steelblue", "FG3M" = "darkorange", "FTM" = "darkgreen")) +
  theme_minimal()

print(p)

# Disconnect
dbDisconnect(con)

print("Done")