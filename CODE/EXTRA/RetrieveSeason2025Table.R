# FILE: RetrieveSeason2025Table.py
# DATE 2025-10-19
# DESCRIPTION: 
# This R program connects to an SQLite database specifically to retrieve 
# basketball data from the Season2025 table. It uses a modern R workflow 
# that allows you to treat a database table as if it were a local data frame.

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
  query <- tbl(con, "Season2025") |>
    select(everything())
  
  # Look at SQL commands that this query builds
  show_query(query)

  print('-------------------------')
  
  # Actually get the Boxscores data -- using collect against the query
  results_df <- query |>
    collect()
  
  # Disconnect
  dbDisconnect(con)
  
  print(results_df, width = Inf)
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