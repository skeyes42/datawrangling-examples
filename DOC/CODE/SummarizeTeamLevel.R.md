## SummarizeTeamLevel.R

This R program calculates and stores the season summary statistics for a set of basketball teams. It moves from detailed, player-level data to high-level, team-level averages and total wins, then saves these results as a new, clean table in the database.

Here is an explanation of its operations for **2026**:

**1. Data Validation**

The script uses dbListFields() to confirm the Boxscores table contains the necessary PTS column.

This safety check ensures that the subsequent calculations won't fail due to missing data. If the column is missing, the program stops immediately and provides instructions on which prerequisite scripts need to be run.

**2. Multi-Stage Aggregation (The Analysis)**

The program employs the dplyr package to perform a complex, two-stage data aggregation using "lazy evaluation" via dbplyr:

**Stage 1 (Game Level)**: It groups data by TEAM_ID and GAME_ID. It calculates the average shooting percentages (FG_PCT_AVG, etc.) for each specific game and extracts the WIN_LOSS outcome.

**Stage 2 (Season Level)**: It then groups *those* results by TEAM_ID alone to calculate:

The overall seasonal average shooting percentages.

The SEASON_WINS by summing the game outcomes.

**Enrichment**: Finally, it performs a left_join with the Teams table to attach the full TEAM_NAME (e.g., "Lakers") to the summary data, replacing the generic TEAM_ID (e.g., "LAL").

**3. Database Interaction and Output**

**show_query(query)**: This command reveals the complex SQL query that dplyr automatically generates and sends to the database engine for efficient processing.

**collect()**: The results of the database-side computation are pulled into R's memory as the results_df.

**dbWriteTable(..., name = "Season2025")**: The core action is saving this new summary data frame as a dedicated table named Season2025 within the existing database file. overwrite = TRUE ensures the table is always current.

**write_csv(...)**: The script also exports the final data to teams_with_name.csv for easy sharing or use in other software (like Excel).

**Summary for 2026**

This script is a sophisticated data processing pipeline. It creates a highly summarized and clean table of seasonal statistics from raw data, demonstrating a robust and efficient way to manage data science workflows in R by pushing computations down to the database level.
