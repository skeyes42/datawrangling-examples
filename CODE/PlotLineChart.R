# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_23_PlotLineChart.R
# DATE 2025-10-26
# DESCRIPTION: 

# Load required libraries
library(RSQLite)
library(ggplot2)
library(dplyr)
library(ggrepel)

path_to_scripts <- Sys.getenv("EXAMPLES")

# Connect to database
path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Query the data
season_data <- dbGetQuery(con, "SELECT FG3_PCT_AVG, SEASON_WINS FROM Season2025")

# Close the database connections
dbDisconnect(con)

# Create the line plot
p <- ggplot(season_data, aes(x = SEASON_WINS, y = FG3_PCT_AVG)) +
  geom_line(color = "#1f77b4", size = 1.2) +
  geom_point(color = "#1f77b4", size = 3, alpha = 0.7) +
  labs(
    title = "3-Point Field Goal Percentage vs Season Wins",
    subtitle = "2025 Season",
    x = "Season Wins",
    y = "Average 3-Point FG %"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(face = "bold", size = 16),
    plot.subtitle = element_text(size = 12, color = "gray40"),
    axis.title = element_text(face = "bold", size = 12),
    panel.grid.minor = element_blank()
  )

  print(p)
