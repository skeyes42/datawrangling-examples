# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: SimpleJoinBoxscoresDB.R
# DATE 2025-10-13
# DESCRIPTION: 
# This R program performs a database table join and data enrichment task. 
# It takes a raw basketball statistics table and merges it with descriptive 
# information (Player and Team names) to create a more useful dataset.

library(RSQLite)
library(DBI)
library(dplyr)
library(readr)

path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")

# Connect to database
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Bring into Boxscores the player and team names
query <- tbl(con, "Boxscores")                    |>
  left_join(tbl(con, "Players"), by = "PLAYER_ID") |>
    left_join(tbl(con, "Teams"), by = "TEAM_ID")   |>
        arrange(GAME_ID, TEAM_ID) |>
          select(-PLAYER_ID, -TEAM_ID)

   
# Display the query
show_query(query) 

# Run the query
results_df <- query |>
  collect()

# Write back to database, replacing the old Boxscores table
dbWriteTable(con, "Boxscores", results_df, overwrite = TRUE)

# Disconnect database connection
dbDisconnect(con)

# Review results of join
print(results_df, width = Inf)

