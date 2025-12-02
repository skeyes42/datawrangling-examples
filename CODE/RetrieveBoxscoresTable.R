# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_2_RetrieveBoxscoresTable.R
# DATE 2025-10-13
# DESCRIPTION: 

library(RSQLite)
library(DBI)
library(dplyr)

# Connect to database with error handling
path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")

tryCatch({
  # Check if file exists first
  if (!file.exists(path_to_database)) {
    stop(sprintf("Database file not found at: %s", path_to_database))
  }
  
  con <- dbConnect(RSQLite::SQLite(), path_to_database)
  
  # Get all data from Boxscores table
  query <- tbl(con, "Boxscores") |>
    select(everything())
  
  # Look at SQL commands that this query builds
  show_query(query)

  print('-------------------------')
  
  # Actually get the Boxscores data -- using collect against the query
  results_df <- query |>
    collect()
  
  # Disconnect
  dbDisconnect(con)
  
  print(results_df)
  print("Done")
  
}, error = function(e) {
  cat("Error occurred:\n")
  cat(sprintf("  Message: %s\n", e$message))
  cat(sprintf("  Attempted path: %s\n", path_to_database))
  
  # Ensure connection is closed if it was opened
  if (exists("con") && dbIsValid(con)) {
    dbDisconnect(con)
  }
})