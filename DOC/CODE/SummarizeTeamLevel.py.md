## SummarizeTeamLevel.py

This Python program processes basketball statistics to generate a team-level performance summary for a specific season. It extracts raw data from an SQLite database, performs multi-level aggregations using **pandas**, and saves the summarized results into a new database table.

**1. Database Connection and Validation**

**Environment Variable**: The script retrieves the database path from an environment variable named EXAMPLES. It includes a check to ensure this variable is set before proceeding.

**Column Verification**: It uses the SQL command PRAGMA table_info to inspect the Boxscores table. It specifically checks for a PTS column to verify that the database has been properly initialized by previous scripts. If the column is missing, it exits with an error.

**2. Data Aggregation (The Analysis)**

The program performs a two-stage aggregation to translate individual boxscores into seasonal team stats:

**Stage 1: Game-Level Summary**:

It groups data by TEAM_ID and GAME_ID.

It calculates the average field goal, three-point, and free-throw percentages for that specific game.

It determines if the game was won by taking the max of the WIN_LOSS column (where a 1 indicates a win).

**Stage 2: Season-Level Summary**:

It groups the game-level results by TEAM_ID.

It calculates the average shooting percentages across all games in the season.

It sums the GAME_WIN values to calculate the total SEASON_WINS for each team.

**3. Database Persistence**

**Table Creation**: The program uses to_sql to create a new table named **Season2025** inside the database.

**if_exists='replace'**: This ensures that if the table already exists, it is overwritten with the most recent calculations.

**Cleanup**: It closes the database connection to ensure data integrity and free up system resources.

**Summary of Output for 2026**

When you run this in 2026, the program will output a DataFrame to your console showing each team's average shooting accuracy and their total win count. Additionally, your Boxscores.db file will now contain a permanent **Season2025** table that can be queried by other applications or R scripts. sqlite3 Documentation \| pandas.DataFrame.to_sql
