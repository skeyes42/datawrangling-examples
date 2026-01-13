# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: FunctionToAccessBoxscores.R
# DATE 2025-10-15
# DESCRIPTION: 
# This R program is a straightforward data utility function designed 
# to extract the complete contents of the "Boxscores" table from a 
# SQLite database and load them into R's memory.

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

print(df)
print("Done")