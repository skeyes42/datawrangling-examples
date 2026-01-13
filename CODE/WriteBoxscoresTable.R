# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: WriteBoxscoresTable.R
# DATE 2025-10-13
# DESCRIPTION: Overwrite Players table 

library(DBI)
library(RSQLite)
library(readr)

path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")

# Connect to a database
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Create dataframe of Players data to write to Boxscores.db
csv_Players_data <- "PLAYER_ID, PLAYER_NAME
1,Fred
2,John
3,Trevor
4,Alex
5,Jim
6,Steve
7,Herb"

Players_data_df <- read_csv(csv_Players_data, 
                     show_col_types = FALSE,
                     col_types = cols(PLAYER_ID = col_integer(), PLAYER_NAME = col_character())
                     )


# Write the data frame to a database table
# The `dbWriteTable()` function creates a new table named "mtcars_data".
# `row.names = FALSE` prevents R from writing the row names as a column.
dbWriteTable(con, "Players", Players_data_df, overwrite = TRUE)


# Verify the table was written by reading it back into R
# The `dbReadTable()` function reads an entire database table.
results_df <- dbReadTable(con, "Players")
print(results_df, width = Inf)


# Clean up: Disconnect from the database
# This step is crucial for managing database resources.
dbDisconnect(con)

print('Done')
