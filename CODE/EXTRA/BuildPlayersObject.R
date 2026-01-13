# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: BuildPlayersObject.R
# DATE 2025-10-16
# DESCRIPTION: 
# This R program is a data extraction tool that pulls information from 
# a specific database table named Players. It uses the modern 
# S7 object-oriented system to organize its code, making it modular 
# and reusable.


library(RSQLite)
library(DBI)
library(S7)
library(dplyr)

Players <- new_class(
  "Players",
  properties = list(
    path = new_property(class_character)
  ),
  # Custom constructor to set the path property
  constructor = function(path_to_database = character()) {
    new_object(S7_object(), path = path_to_database)
  }
)

# Create a new generic function for retrieving the data frame
players_dataframe <- new_generic("players_dataframe", "x")

method(players_dataframe, Players) <- function(x) {

  con <- dbConnect(RSQLite::SQLite(), x@path)
  
  query <- tbl(con, "Players")
    
  results_df <- query |>
    collect()
    
  dbDisconnect(con)
    
    return(results_df)
}

get_Players_instance <- function(db_path) {
  Players(path_to_database = db_path)
}

# Set path to Players database
path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")

# Instantiate the Players class
players_object <- get_Players_instance(path_to_database)

# Call the players_dataframe() method to get the data
players_data <- players_dataframe(players_object)

# View the resulting data frame
print(players_data)

print('Done')