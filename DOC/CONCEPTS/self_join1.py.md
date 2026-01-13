## self_join1.py

This Python program uses the

**pandas** library to create, manipulate, and restructure a basketball statistics dataset using a **self-join**.

The primary purpose of this specific script is to illustrate *how* a self-join creates every possible pairing of teammates within the same game and then demonstrates how you might access those separated columns for analysis.

How the Program Works

**Data Creation:**

A pandas DataFrame called boxscores is created. It lists individual player statistics (FGM, FGA, etc.) across different games (GAME_ID) and teams (TEAM_ID).

**The Core Logic: Self-Join**

teammate_pairs = boxscores.merge(...): This line merges the boxscores DataFrame with itself.

**on=['GAME_ID', 'TEAM_ID']**: This is the critical condition. It ensures that a row for Player 1 only links up with a row for Player 2 if they share the exact same GAME_ID *and* the same TEAM_ID—meaning they were teammates in that specific game.

**suffixes=('_p1', '_p2')**: Because both sides of the join have identical column names (like FGM), pandas appends \_p1 to the first player's stats and \_p2 to the second player's stats (e.g., FGM_p1, FGM_p2).

**Restructuring and Output:**

The second half of the script (key_cols, p1_cols, df_p1, df_p2) is purely for presentation. It separates the resulting large teammate_pairs DataFrame into two new DataFrames (df_p1 and df_p2) to visually isolate the stats of the "first player" and the "second player" for easier viewing, then prints them in Markdown format.

Summary of the Output

The self-join expands the 12-row dataset into a much larger table (48 rows). For Game 1000, which has 4 player rows, it creates

![](media/325472601571f31e1bf00674c368d335.gif)

$$
4 \times 4 = 1 6
$$

4×4=16

unique pairings.

The final printed DataFrames (df_p1 and df_p2) will show that for every player:

They are listed once matched up against themselves.

They are listed matched up against every one of their actual teammates.

In a real analytical scenario, you would typically add filters to this result to remove the "player matched with self" rows and eliminate duplicate pairs (e.g., filtering to ensure PLAYER_ID_p1 \< PLAYER_ID_p2).
