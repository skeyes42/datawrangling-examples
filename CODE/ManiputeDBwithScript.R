# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_25_FunctionToManiputeDB.R
# DATE 2025-10-26
# DESCRIPTION: 

library(DBI)
library(RSQLite)
library(readr)

# Create connection to database
path_to_database <- paste0(Sys.getenv("EXAMPLES"), "Boxscores.db")
con <- dbConnect(RSQLite::SQLite(), path_to_database)


# Setup path_to_script
path_to_scripts <- Sys.getenv("EXAMPLES")

# Change working directory
setwd(path_to_scripts)

# Get list of tables before
before <- dbListTables(con)
print('--- before ---')
print(before)

# # Drop all tables
system("sqlite3 Boxscores.db '.read drop_all_tables.sql'")

# Get list of tables after dropping
after <- dbListTables(con)
print('--- after dropping ---')
print(after)

# # Recreate tables
system("sqlite3 Boxscores.db '.read boxscores.sql'")

# Get list of tables after recreation
after <- dbListTables(con)
print('--- after recreating ---')
print(after)

# Disconnect
dbDisconnect(con)

print("Done")

