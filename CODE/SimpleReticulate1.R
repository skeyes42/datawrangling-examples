# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: SimpleReticulate.R
# DATE 2025-10-16
# DESCRIPTION: 
# This R program utilizes the reticulate library to bridge R and Python 
# environments, allowing R code to seamlessly execute Python functions 
# and access powerful Python data science libraries like pandas and nba_api.

library(reticulate)

# Define your Python code as a multi-line string
python_code <- "
import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import time

def get_player_id(player_name):
   
    nba_players = players.get_players()

    player_id = []
    for player in nba_players:
        if player['full_name'] == player_name:
            player_id.append(player)

    
    if player_id:
        return player_id[0]['id']
    return None
"

# Execute the Python code within the R session
py_run_string(python_code)

# Now, you can call the Python function directly from R
player_name <- "Stephen Curry"
player_id <- py$get_player_id(player_name)

# You can now use the player_id in R, for example:
if (!is.null(player_id)) {
  print(paste("Player ID for", player_name, "is:", player_id))
} else {
  print(paste("Player ID for", player_name, "not found."))
}

