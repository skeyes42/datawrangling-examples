# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_10_AnonymousFunctions.py
# DATE 2025-10-15
# DESCRIPTION: Python conversion of R boxscores analysis

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def get_boxscores(path_to_database):
    # Connect to database
    con = sqlite3.connect(path_to_database)
    
    # Query the Boxscores table
    query = "SELECT * FROM Boxscores"
    results_df = pd.read_sql_query(query, con)
    
    con.close()
    return results_df

# Get path to database
path_to_database = os.path.join(os.getenv("EXAMPLES"), "Boxscores.db")
df = get_boxscores(path_to_database)

# Store the valid answers in a list
valid_answers = ["1", "2", "3"]

# Display the question and options to the user
print("Please select an option:")
print("1. View means")
print("2. View Boxscores table")
print("3. Plot")

# Prompt the user for input
choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
    # Calculate means grouped by GAME_ID and TEAM_ID
    mean_df = df.groupby(['GAME_ID', 'TEAM_ID'])[['FGM', 'FG3M', 'FTM']].mean().reset_index()
    
    # Display the dataframe
    print("\nMeans by Game and Team:")
    print(mean_df)
    # Alternative: mean_df.to_csv('means_output.csv', index=False)

elif choice == "2":
    # Calculate scoring effort using lambda function
    scoring_df = df.copy()
    scoring_df['SCORING_EFFORT'] = scoring_df.apply(
        lambda row: row['FGM'] + row['FG3M'] + row['FTM'], axis=1
    )
    
    # Display the dataframe
    print("\nBoxscores with Scoring Effort:")
    print(scoring_df)
    # For interactive table viewing, you could use:
    # from IPython.display import display
    # display(scoring_df)

elif choice == "3":
    # Calculate scoring effort
    scoring_df = df.copy()
    scoring_df['SCORING_EFFORT'] = scoring_df.apply(
        lambda row: row['FGM'] + row['FG3M'] + row['FTM'], axis=1
    )
    
    # Create boxplot
    plt.figure(figsize=(10, 6))
    
    # Create the boxplot
    sns.boxplot(data=scoring_df, x='WIN_LOSS', y='SCORING_EFFORT', 
                hue='WIN_LOSS', palette='Set2', legend=False)
    
    # Add labels and title
    plt.title('Scoring Effort by Win/Loss Outcome', fontsize=14, 
              fontweight='bold')
    plt.xlabel('Game Outcome', fontsize=12)
    plt.ylabel('Scoring Effort', fontsize=12)
    
    # Use minimal theme
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.tight_layout()
    
    # Display the plot
    plt.show()

print('Done')