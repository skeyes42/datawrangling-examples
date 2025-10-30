# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_9_FunctionToAccessBoxscores.R
# DATE 2025-10-15
# DESCRIPTION: 

library(RSQLite)
library(DBI)
library(dplyr)

# Define the function
getBoxscores <- function(path_to_database) {

  con <- dbConnect(RSQLite::SQLite(), path_to_database)
  
  query <- tbl(con, "Boxscores") |>
             select(everything())
    
  results_df <- query |>
    collect()
  
  dbDisconnect(con)

  return(results_df)
  
}

# Use the function
path_to_database <- paste0(Sys.getenv("EXAMPLES"), "Boxscores.db")

df <- getBoxscores(path_to_database)

View(df)

print("Done")