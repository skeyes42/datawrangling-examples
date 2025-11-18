# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_28_Correlation.R
# DATE 2025-11-01
# DESCRIPTION: 

library(dplyr)
library(RSQLite)
library(DBI)

# Connect to database
path_to_database <- paste0(Sys.getenv("EXAMPLES"), "Boxscores.db")
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
print(correlation_matrix)
