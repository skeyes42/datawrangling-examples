# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_15_SimpleReticulate.py
# DATE 2025-10-16
# DESCRIPTION: 

import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import time

def get_player_id(player_name):
    """
    Retrieves the player ID from the NBA API.
    Returns the player ID if found, otherwise None.
    """
    nba_players = players.get_players()

    player_id = []
    for player in nba_players:
        if player['full_name'] == player_name:
            player_id.append(player)

    
    if player_id:
        return player_id[0]['id']
    return None

id = get_player_id("LeBron James")

print(id)
