## self_join.R

This program demonstrates a

**self-join** using the R **dplyr** package. A self-join occurs when you join a table with itself, creating every possible combination of rows that share a common value—in this case, the GAME_ID.

How it Works

**The Dataset:** The df contains boxscore stats (Field Goals Made, 3-Pointers, etc.) for players across two different games (1000 and 2000).

**The Join Logic (left_join):** The program links the table to itself using GAME_ID as the key.

For every row in the original table, it finds **every other row** in the same table that has the same GAME_ID.

This effectively creates a list of "teammates and opponents" for every player performance.

**The Suffixes:** Because both tables have the same column names (like PLAYER_ID or FGM), the suffix = c("", "x") argument is used to distinguish them.

Columns from the "left" side keep their original names.

Columns from the "right" side get an **"x"** added to the end (e.g., PLAYER_IDx, FGMx).

The Result

The output dataframe will be much larger than the original because it generates **permutations**.

**Game 1000** has 4 entries. In a self-join, each of those 4 entries will match with all 4 entries of Game 1000 (including itself). This results in

![](media/325472601571f31e1bf00674c368d335.gif)

$$
4 \times 4 = 1 6
$$

4×4=16

rows for Game 1000.

**Game 2000** also has 4 entries, resulting in another 16 rows.

The final df_self_join will have **32 rows** total.

Why use this?

In sports analytics, this technique is commonly used to:

**Compare teammates:** See how Player A performed compared to Player B in the same game.

**Matchups:** Compare a player's stats against the stats of every player on the opposing team.

**Calculations:** Calculate a player's "share" of the team's total points or rebounds by comparing their row to all other rows in that game.
