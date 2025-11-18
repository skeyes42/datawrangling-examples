# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_0_GetBoxscoresDBinfo.R
# DATE 2025-10-19
# DESCRIPTION: 

library(DBI)
library(RSQLite)

path_to_database <- paste0(Sys.getenv("EXAMPLES"), "Boxscores.db")

# Establish a connection to the SQLite database
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Get table names
table_names <- dbListTables(con)
print(table_names)

print('--------------------------------------------------------------')

# Setup table name
table_name <- "Boxscores" 

# Execute the PRAGMA statement to get table info
column_info <- dbGetQuery(con, paste0("PRAGMA table_info(", table_name, ");"))

# Print the column names
print(column_info)

# Disconnect from the database
dbDisconnect(con)