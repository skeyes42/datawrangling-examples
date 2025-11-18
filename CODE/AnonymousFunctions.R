# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_10_AnonymousFunctions.R
# DATE 2025-10-15
# DESCRIPTION: 

library(RSQLite)
library(DBI)
library(dplyr)
library(tidyverse)
library(rhandsontable)
library(ggplot2)

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

path_to_database <- paste0(Sys.getenv("EXAMPLES"), "Boxscores.db")
df <- getBoxscores(path_to_database)

# Store the valid answers in a vector
valid_answers <- c("1", "2", "3")

# Initialize a variable for the user's choice
choice <- NULL

# Display the question and options to the user
cat("Please select an option:\n")
cat("1. View means\n")
cat("2. View Boxscores table\n")
cat("3. Plot\n")

# Prompt the user for input and read one line
choice <- readline("Enter your choice (1, 2, or 3): ")

if(choice == 1) {

  mean_df <- df |>
    group_by(GAME_ID, TEAM_ID) |>
      summarize(across(c(FGM, FG3M, FTM),\(x) mean(x))) |>  #Lambda syntax
        ungroup() 
      
  print(mean_df)
}

if(choice == 2) {
  
  scoring_df <- df |>
    mutate(SCORING_EFFORT = pmap_dbl(list(FGM, FG3M, FTM),sum))
  
  print(
    rhandsontable(scoring_df)
  )

}
  
if(choice == 3) {

  scoring_df <- df |>
    mutate(SCORING_EFFORT = pmap_dbl(list(FGM, FG3M, FTM),sum))

  print(
    ggplot(data = scoring_df, 
        mapping = aes(x = as.factor(WIN_LOSS), y = SCORING_EFFORT)) +
      geom_boxplot(aes(fill = as.factor(WIN_LOSS))) +
      labs(
        title = "Scoring Effort by Win/Loss Outcome",
        x = "Game Outcome",
        y = "Scoring Effort"
      ) +
      theme_minimal()
  )

}

print('Done')