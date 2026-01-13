## Correlation.py

This Python program is a statistical analysis tool designed to identify relationships between different basketball performance metrics using a **correlation matrix**.

**1. Data Retrieval**

**Database Path**: The program retrieves the database location from a system environment variable named EXAMPLES. It targets a file named Boxscores.db.

**Loading**: It uses the sqlite3 library to connect to the database and Pandas to load the entire Boxscores table into a memory-efficient DataFrame.

**Cleanup**: Immediately after loading the data, it closes the database connection to free up system resources.

**2. Data Preparation**

Before performing the analysis, the script cleans the table by removing specific columns:

**Excluded Columns**: It drops GAME_ID, PLAYER_ID, and TEAM_ID.

**Why?**: These are identification numbers (metadata), not performance statistics. Including them in a statistical calculation would result in meaningless data (e.g., trying to find the correlation between a Player's ID number and their 3-point percentage).

**3. Statistical Analysis: Correlation Matrix**

The core of the program is the results_df.corr() function:

**The Calculation**: It calculates the "Pearson correlation coefficient" for every pair of statistics (like Points vs. Rebounds or Field Goal Attempts vs. Assists).

**numeric_only=True**: This ensures the program only attempts to calculate correlations for columns containing numbers, skipping any text-based data (like player names) that might remain.

**The Result**: The output is a grid (matrix) where:

**1.0**: Perfect positive correlation (as one stat goes up, the other always goes up).

**0.0**: No relationship at all.

**-1.0**: Perfect negative correlation (as one stat goes up, the other always goes down).

**Summary**

This script is used by analysts to answer questions like: *"Is there a strong relationship between the number of assists and the number of points scored?"* or *"Do players who take more 3-pointers tend to have more or fewer rebounds?"* It provides a high-level overview of how different parts of the game are linked together in your 2026 dataset.
