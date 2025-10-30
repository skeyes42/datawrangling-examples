# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_1_LoadBoxscoresTable.R
# DATE 2025-10-12
# DESCRIPTION: Load table from csv file.

library(RSQLite)
library(DBI)
library(readr)

# Set up paths to resources
path_to_data     <- Sys.getenv("EXAMPLES")
path_to_database <- paste0(path_to_data, "boxscores.db")
path_to_csv      <- paste0(path_to_data, "boxscores.csv")

# Get connection
db_connection <- dbConnect(RSQLite::SQLite(), path_to_database)

# Get boxscore dataframe from csv file
df_boxscores <- read_csv(path_to_csv)

# Append data to Boxscores table
dbAppendTable(db_connection, "Boxscores", df_boxscores)

# Disconnect
dbDisconnect(db_connection)

# View the boxscore data you just loaded
View(df_boxscores)

print("Done")
