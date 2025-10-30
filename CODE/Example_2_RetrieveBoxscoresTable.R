# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_2_RetrieveBoxscoresTable.R
# DATE 2025-10-13
# DESCRIPTION: 

library(RSQLite)
library(DBI)
library(dplyr)

# Connect to database
path_to_database <- paste0(Sys.getenv("EXAMPLES"), "Boxscores.db")
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