## joins.R

This R program demonstrates how to merge two datasets using the **dplyr** library. It uses a list of players (players_df) and a list of game statistics (boxscores_df) to show the four primary types of SQL-style joins.

The datasets contain two intentional "mismatches" to highlight how joins work:

**Michael (ID 7):** Exists in the player list but has no game data.

**Player ID 99:** Exists in the game data but has no name in the player list.

**1. Inner Join**

**inner_join(boxscores_df, players_df)**

**Result:** Only returns rows where the PLAYER_ID exists in **both** tables.

**Excluded:** Michael (ID 7) and Player 99 are both dropped because they don't have a matching pair in the other table.

**2. Left Join**

**left_join(boxscores_df, players_df)**

**Result:** Keeps **all rows from the first table** (boxscores_df).

**Outcome:** Player 99 is included. However, since there is no name for ID 99 in the player table, the PLAYER_NAME column will show NA (null). Michael is excluded because he is not in the boxscores.

**3. Right Join**

**right_join(boxscores_df, players_df)**

**Result:** Keeps **all rows from the second table** (players_df).

**Outcome:** Michael (ID 7) is included. Because he has no game data, his statistics (FGM, FG3M, etc.) will show as NA. Player 99 is excluded because they aren't in the player list.

**4. Full Join**

**full_join(boxscores_df, players_df)**

**Result:** Keeps **every row from both tables**, regardless of whether there is a match.

**Outcome:** This is the most inclusive join. You will see Michael with NA stats AND Player 99 with an NA name. No data is lost.

**Summary of Keys**

| **Join Type** | **Records Kept**                     |
|---------------|--------------------------------------|
| **Inner**     | Only matches                         |
| **Left**      | All boxscores + names if available   |
| **Right**     | All players + boxscores if available |
| **Full**      | Everything from both tables          |
