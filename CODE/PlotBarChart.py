# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_22_PlotBarChart.py
# DATE 2025-10-27
# DESCRIPTION: 

import sqlite3
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the database
path_to_database = os.path.join(os.getenv("EXAMPLES", ""), "Boxscores.db")
try:
    con = sqlite3.connect(path_to_database)
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    con = None

if con:
    # Build query using pandas and execute
    # pandas uses pd.read_sql_query to run a SQL query directly on a database connection
    # and return the result as a DataFrame.
    sql_query = """
    SELECT
        T1.GAME_ID,
        T1.TEAM_ID,
        T2.PLAYER_NAME AS Player,
        T3.TEAM_NAME AS Team,
        T1.FGM,
        T1.FG3M,
        T1.FTM
    FROM
        Boxscores AS T1
    LEFT JOIN
        Players AS T2 ON T1.PLAYER_ID = T2.PLAYER_ID
    LEFT JOIN
        Teams AS T3 ON T1.TEAM_ID = T3.TEAM_ID
    WHERE
        Player = 'John'
    ORDER BY
        T1.GAME_ID, T1.TEAM_ID
    """

    try:
        results_df = pd.read_sql_query(sql_query, con)
    except pd.io.sql.DatabaseError as e:
        print(f"Error executing SQL query: {e}")
        results_df = pd.DataFrame()

    # Reshape the data from wide to long format using pandas.melt()
    results_long_df = pd.melt(
        results_df,
        id_vars=["GAME_ID", "Team", "Player"],
        value_vars=["FGM", "FG3M", "FTM"],
        var_name="Stat_Type",
        value_name="Count"
    )

    # Create the grouped bar chart using seaborn and matplotlib
    # Seaborn is a high-level plotting library built on matplotlib that is 
    # well-suited for statistical graphics.
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x="GAME_ID",
        y="Count",
        hue="Stat_Type",
        data=results_long_df,
        palette={"FGM": "steelblue", "FG3M": "darkorange", "FTM": "darkgreen"}
    )
    plt.title("FGM, FG3M, and FTM by Game for John")
    plt.xlabel("Game ID")
    plt.ylabel("Count")
    plt.legend(title="Statistic")
    plt.show()

    # Disconnect
    con.close()

    print("Done")

