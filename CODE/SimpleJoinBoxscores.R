# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_5_SimpleJoinBoxscoresDB.R
# DATE 2025-10-13
# DESCRIPTION: 

library(RSQLite)
library(DBI)
library(dplyr)

path_to_database <- paste0(Sys.getenv("EXAMPLES"), "Boxscores.db")

# Connect to database
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Bring into Boxscores the player and team names
query <- tbl(con, "Boxscores")    |>
  left_join(tbl(con, "Players")   |> rename(Player = PLAYER_NAME), 
      by = "PLAYER_ID") |>
    left_join(tbl(con, "Teams")   |> rename(Team = TEAM_NAME),     
        by = "TEAM_ID")   |>
        arrange(GAME_ID, TEAM_ID) |>
          select(-PLAYER_ID, -TEAM_ID)

   
# Display the query
show_query(query) 

# Run the query
results_df <- query |>
  collect()

# Disconnect database connection
dbDisconnect(con)

# Review results of join
print(results_df)
