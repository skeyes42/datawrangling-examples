# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: PlotBoxChart.R
# DATE 2025-11-13
# DESCRIPTION: 
# This R program is the functional equivalent of the Python script you 
# previously shared. It retrieves sports data from a database, calculates 
# a combined scoring metric, and generates a boxplot to compare 
# performance between wins and losses.

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

path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")
df <- getBoxscores(path_to_database)

  scoring_df <- df |>
    mutate(SCORING_EFFORT = pmap_dbl(list(FGM, FG3M, FTM),sum))

print(
  ggplot(data = scoring_df,
      mapping = aes(x = as.factor(WIN_LOSS), y = SCORING_EFFORT)) +
    geom_boxplot(aes(fill = as.factor(WIN_LOSS))) +
    scale_fill_grey() +  # Add this line
    scale_x_discrete(labels = c("0" = "Loss", "1" = "Win")) +
    labs(
      title = "Scoring Effort by Win/Loss Outcome",
      x = "Game Outcome",
      y = "Scoring Effort"
    ) +
    theme_minimal()
)


print('Done')