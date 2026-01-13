# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Correlation.R
# DATE 2025-11-01
# DESCRIPTION: 
# This R program is a statistical script designed to calculate a correlation 
# matrix for basketball performance metrics. It identifies how strongly 
# different statistics (like points, assists, and rebounds) are related to 
# one another.

library(dplyr)
library(RSQLite)
library(DBI)

# Connect to database
path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Get selected numeric variables from Boxscores table
query <- tbl(con, "Boxscores") |>
  select(-GAME_ID, -PLAYER_ID, -TEAM_ID)

# Actually get the Boxscores data -- using collect against 
# the query
results_df <- query |>
  collect()

# Disconnect
dbDisconnect(con)

# Calculate the correlation matrix for only the numeric columns
correlation_matrix <- results_df |>
  select(where(is.numeric)) |>
  cor(use = "complete.obs") # handles missing values if any

# View the result
options(width = 200)
print(correlation_matrix)
