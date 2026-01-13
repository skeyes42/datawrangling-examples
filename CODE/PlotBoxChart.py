# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: PlotBoxChart.py
# DATE 2025-11-13
# DESCRIPTION: 
# This Python program extracts sports data from a database, calculates a custom 
# performance metric, and generates a boxplot to compare performance between 
# wins and losses. It is essentially a Python version of an R/ggplot2 workflow 
# using the plotnine library.

import os
import sqlite3
import pandas as pd
from plotnine import *

# Define the function
def get_boxscores(path_to_database):
    """Connects to SQLite and reads the Boxscores table into a DataFrame."""
    # Connect to the database
    con = sqlite3.connect(path_to_database)
    
    # Read entire table (equivalent to tbl |> select(everything) |> collect)
    query = "SELECT * FROM Boxscores"
    results_df = pd.read_sql_query(query, con)
    
    # Close connection
    con.close()
    
    return results_df

# Get path from environment variable
path_to_database = os.path.join(os.environ.get("EXAMPLES", ""), "Boxscores.db")
df = get_boxscores(path_to_database)

# Calculate SCORING_EFFORT (equivalent to pmap_dbl sum)
# We sum the specific columns across axis 1 (rows)
df['SCORING_EFFORT'] = df[['FGM', 'FG3M', 'FTM']].sum(axis=1)

# Create the plot using plotnine (Python's ggplot2)
p = (

    ggplot(df, aes(x='factor(WIN_LOSS)', y='SCORING_EFFORT'))
    + geom_boxplot(aes(fill='factor(WIN_LOSS)'))
    + scale_fill_grey() #
    + scale_x_discrete(labels={"0": "Loss", "1": "Win"}) #
    + labs(
        title="Scoring Effort by Win/Loss Outcome",
        x="Game Outcome",
        y="Scoring Effort"
    )
    + theme_minimal()
)
# Save the plot
p.save("scoring_effort_boxplot.png", width=8, height=6, dpi=300)

print('Done')
