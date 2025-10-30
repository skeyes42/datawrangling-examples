# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_23_PlotLineChart.py
# DATE 2025-10-26
# DESCRIPTION: 

import os
import sqlite3
import pandas as pd
from plotnine import (
    ggplot,
    aes,
    geom_line,
    geom_point,
    labs,
    theme_minimal,
    scale_color_brewer,
)

# Connect to database
path_to_database = os.path.join(os.getenv("EXAMPLES", ""), "Boxscores.db")
con = sqlite3.connect(path_to_database)

# Build query that will do joins
query = """
    SELECT
        T1.GAME_ID,
        T1.FGM,
        T1.FG3M,
        T1.FTM,
        T2.PLAYER_NAME AS Player,
        T3.TEAM_NAME AS Team
    FROM Boxscores AS T1
    LEFT JOIN Players AS T2 ON T1.PLAYER_ID = T2.PLAYER_ID
    LEFT JOIN Teams AS T3 ON T1.TEAM_ID = T3.TEAM_ID
    WHERE T2.PLAYER_NAME = 'John'
    ORDER BY T1.GAME_ID, T1.TEAM_ID
"""

# Run the query and collect results into a pandas DataFrame
results_df = pd.read_sql(query, con)

# Select and filter the data for the specific player
player1_stats = results_df[['GAME_ID', 'FGM', 'FG3M', 'FTM']]

# Reshape the data from wide to long format using pandas.melt
player1_long = player1_stats.melt(
    id_vars=['GAME_ID'],
    var_name='statistic',
    value_name='value'
)

# Create the line plot with plotnine
p = (
    ggplot(player1_long, aes(x='GAME_ID', y='value', color='statistic'))
    + geom_line(size=1.2)
    + geom_point(size=3)
    + labs(
        title="John's Scoring Statistics Over Time",
        subtitle="Comparing Field Goals, 3-Pointers, and Free Throws Made",
        x="Game ID",
        y="Count",
        color="Statistic"
    )
    + theme_minimal()
    + scale_color_brewer(type='qual', palette="Set1")
)

# Save the plot
p.save('/home/stevie/DLUBU/EXAMPLES/DATA/Boxscores/johns_scoring_stats.png')

# Clean up database connection
con.close()
