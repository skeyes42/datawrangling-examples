## SelfJoinBuildWinLoss.R

This R program is a data enrichment pipeline for a basketball database. Its primary purpose is to calculate team scores and determine game winners, then save those results back into the database and a CSV file.

In the context of **2026**, this script follows modern R best practices for database interaction and tidy data manipulation.

**1. Prerequisite Validation**

The program begins with a safety check using dbListFields(). It looks for the PTS (points) column in the **Boxscores** table. If it isn't found, the program stops immediately. This prevents the following logic from failing when it tries to sum non-existent data.

**2. Calculating Team Scores (Summarization)**

Using dplyr syntax on a database object (tbl), it aggregates player-level data into team totals:

It groups the data by GAME_ID and TEAM_ID.

It sums the PTS to create a new SCORE variable.

**3. The "Self-Join" Win/Loss Logic**

This is the most complex part of the script. To figure out who won, the program must compare a team's score against their opponent's score in the same game:

**The Join**: It joins the scores table to itself using GAME_ID.

**The Filter**: It uses filter(TEAM_ID_team != TEAM_ID_opponent) to ensure a team isn't being compared to itself.

**The Logic**: It uses case_when() to create a WIN_LOSS flag:

**1** if the team score is higher (Win).

**0** if the team score is lower (Loss).

**Cleanup**: It uses stringr to clean up the column suffixes (removing \_team), resulting in a clean table of GAME_ID, TEAM_ID, SCORE, and WIN_LOSS.

**4. Data Integration and Persistence**

**Merging**: The program takes the original player-level data (boxscores_df) and performs a left_join with the new results_df. This assigns the team score and the win/loss outcome to every individual player's row.

**Database Update**: It uses dbWriteTable() with overwrite = TRUE. This replaces the old **Boxscores** table in the SQLite database with the new, enriched version.

**Export**: It saves a final copy of the data to simple_boxscores.csv for use in Excel or other tools.

**5. Key 2026 Technical Features**

**DBI/RSQLite**: Ensures the connection is handled securely and efficiently.

**Lazy Evaluation**: By using show_query(query), the program demonstrates that the heavy lifting of the join and win/loss calculation happens inside the **database engine** (SQL), not in R's memory.

**Native Pipe (\|\>)**: Uses the modern R pipe for better readability and performance.

**Summary of Output**

By the end of the script, your **Boxscores.db** database is updated so that every player row now tells you:

How many total points their **team** scored.

Whether their team **won (1)** or **lost (0)** that specific game. RSQLite Documentation \| dplyr for Databases
