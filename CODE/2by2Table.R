# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: 2by2Table.R
# DATE 2025-11-01
# DESCRIPTION: 
# This R program performs a "database-to-table" workflow by retrieving 
# basketball statistics from a database and organizing them into a 
# formatted frequency table.

library(dplyr)
library(RSQLite)
library(DBI)
library(janitor)

# Connect to database
path_to_database <- paste0(Sys.getenv("EXAMPLES"), "Boxscores.db")
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Get selected numeric variables from Boxscores table
query <- tbl(con, "Boxscores") |>
           select(FGM, FG3M)

# Actually get the Boxscores data -- using collect against the query
results_df <- query |>
  collect()

# Disconnect
dbDisconnect(con)

# Convert numeric columns to 2x2 factor variables
# Example: Categorize based on a threshold (e.g., > 2 made)
processed_data <- results_df |>
  mutate(
    FG3M_category = factor(ifelse(FG3M > 2, "High 3P", "Low 3P"), 
      levels = c("Low 3P", "High 3P")),
    FGM_category = factor(ifelse(FGM > 5, "High FG", "Low FG"), 
      levels = c("Low FG", "High FG"))
  )

# 3Generate the 2x2 table using tably()
fg_table <- processed_data |>
  tabyl(FG3M_category, FGM_category)

# Print the table
print(fg_table)
