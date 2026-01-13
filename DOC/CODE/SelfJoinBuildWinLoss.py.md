## SelfJoinBuildWinLoss.py

This program updates a database by calculating game scores and win/loss outcomes for basketball teams, then merging those results back into the main dataset. It essentially automates the "standings" calculation for a set of boxscore data.

Here is the breakdown of its operations for 2026:

**1. Pre-flight Validation**

The program first checks if the PTS (points) column exists in the Boxscores table using the PRAGMA table_info command.

**Safety Logic:** If the column is missing, it prints an error and stops the script (sys.exit(1)). This prevents the program from failing later during complex calculations.

**2. Win/Loss Logic (SQL Self-Join)**

The core of the program is a Common Table Expression (CTE) and a **self-join**:

**Aggregation:** It first sums up the points for every team in every game.

**Comparison:** It joins this list of scores against itself. By matching on GAME_ID but filtering for TEAM_ID != TEAM_ID, it puts a team's score right next to their opponent's score.

**The Winner:** A CASE statement compares the two scores:

If Team A's score \> Team B's score, it assigns a 1 (Win).

If Team A's score \< Team B's score, it assigns a 0 (Loss).

**3. Data Merging (Pandas)**

Once the win/loss results are calculated, the program uses **Pandas** to integrate them:

It loads the original Boxscores table.

It cleans the table by dropping any old SCORE or WIN_LOSS columns to avoid duplicates.

**pd.merge**: It performs a Left Join to attach the new SCORE and WIN_LOSS values to every individual player row based on their GAME_ID and TEAM_ID.

**4. Database Overwrite and Export**

**to_sql with if_exists='replace'**: The program saves the updated, enriched DataFrame back into the SQLite database, completely replacing the old Boxscores table with the new version that now includes outcome data.

**CSV Backup**: Finally, it exports a copy of the updated data to boxscore.csv for external use.

**Summary of 2026 Use Case**

This is a data enrichment script. If you have a database of player stats but don't know who won the games, running this program calculates the team totals and flags every player as having been on the winning or losing side of that specific matchup.
