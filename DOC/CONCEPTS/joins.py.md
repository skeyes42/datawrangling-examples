## joins.py

This Python program demonstrates how to merge datasets using the **pandas** library. It performs the same logic as the R/dplyr version, using pd.merge() to combine a player list (players_df) and game statistics (boxscores_df).

The program uses a **key** (PLAYER_ID) to link the two tables and illustrates the four main types of relational joins:

**1. Inner Join (how='inner')**

**Logic:** Keeps only the rows where the PLAYER_ID exists in **both** DataFrames.

**Result:** It excludes Michael (ID 7) because he didn't play a game, and excludes Player 99 because that ID isn't in the player registry.

**2. Left Join (how='left')**

**Logic:** Keeps every row from the "left" table (boxscores_df).

**Result:** All game records are kept. Player 99 is included, but their PLAYER_NAME will appear as NaN (Not a Number/null) because their name is missing from the player table.

**3. Right Join (how='right')**

**Logic:** Keeps every row from the "right" table (players_df).

**Result:** All registered players are kept. Michael (ID 7) is included, but his game stats (FGM, FTM, etc.) will appear as NaN because he has no entries in the boxscores.

**4. Full/Outer Join (how='outer')**

**Logic:** Keeps **all** rows from both DataFrames.

**Result:** This is the most comprehensive view. It includes both the "unnamed" Player 99 and the "gameless" Michael, filling in NaN wherever data is missing from either side.

**Key Syntax Differences (vs. R)**

**pd.concat**: Used here to add the new row for Player 99 to the boxscores.

**pd.merge**: The universal function for joins in pandas. The how parameter determines the join type (inner, left, right, or outer).
