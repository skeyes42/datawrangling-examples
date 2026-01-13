## self_join.py

This program demonstrates a

**self-join** using the **pandas** library in Python. A self-join is a technique where you merge a DataFrame with itself to compare rows that share a common attribute—in this case, the GAME_ID.

How it Works

**The Input Data:** The DataFrame df represents boxscore statistics for players in two different games (ID 1000 and ID 2000). Each game has four player entries.

**The Merge (df.merge)**:

The program calls df.merge(df, ...) which treats the same dataset as both the "left" and "right" sides of the join.

**on='GAME_ID'**: This tells pandas to match every row in the table with every other row that has the same Game ID.

**The Suffixes**: Since both sides of the join have identical column names (TEAM_ID, PLAYER_ID, FGM, etc.), pandas needs to distinguish them.

**suffixes=('', 'x')**: The left side columns keep their original names, while the right side columns have an **"x"** appended (e.g., PLAYER_IDx, FGMx).

The Resulting Data

The output creates a "pairing" of every player in a game with every other player in that same game (including themselves).

**Row Expansion:** Because Game 1000 has 4 player rows, the self-join creates

![](media/325472601571f31e1bf00674c368d335.gif)

$$
4 \times 4 = 1 6
$$

4×4=16

combinations for that game. The same happens for Game 2000.

**Total Rows:** The original 8-row DataFrame grows to **32 rows** (

![](media/325472601571f31e1bf00674c368d335.gif)

$$
1 6 + 1 6
$$

16+16

).

**Context:** For any single row in the new df_self_join, you can see a player's stats on the left and a "matched" player's stats (teammate or opponent) on the right.

Common Use Cases in 2026

In data science and sports analytics, this specific pandas pattern is used for:

**Calculating Point Spreads:** Comparing a team's score against their opponent's score in the same game.

**Player Comparisons:** Analyzing how Player A performs when Player B is also on the court.

**Network Analysis:** Building a graph of which players have played with or against one another.

.
