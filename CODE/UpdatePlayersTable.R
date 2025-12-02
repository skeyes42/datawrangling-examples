# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_4_UpdatePlayersTable.R
# DATE 2025-10-13
# DESCRIPTION: Update Players table

library(DBI)
library(RSQLite)
library(readr)

path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")

# Connect to a database
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Construct the SQL UPDATE statement
sql_update_query <- "UPDATE Players SET PLAYER_NAME = 'Johnie' WHERE PLAYER_ID = 2;"

# Execute the statement
dbExecute(con, sql_update_query)

# Verify the table was written by reading it back into R
# The `dbReadTable()` function reads an entire database table.
results_df <- dbReadTable(con, "Players")
print(results_df)

# Disconnect from the database
dbDisconnect(con)

print('Done')