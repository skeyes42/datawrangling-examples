## reshaping1.py

Here is the play-by-play of what’s happening:

**1. The Setup (Data Creation)**

The code starts with a dictionary representing players, their teams, and three specific stats (**FGM**: Field Goals Made, **FG3M**: 3-Pointers Made, and **FTM**: Free Throws Made) across two different games.

**2. The "Pivot Wider" (Growth Tracking)**

The script reshapes the data to compare games side-by-side for each player.

-   **What it does:** It moves GAME_ID from rows to columns. Instead of two rows for Player 1, you get one row with columns like FGM_game1000 and FGM_game2000.
-   **The Goal:** This allows the code to calculate "Deltas" (the change in performance) between the two games.

**3. The "Pivot Longer" (Deep Dive)**

The script then melts the data back down into a long format.

-   **What it does:** It turns stat categories (FGM, FG3M, FTM) into a single column called stat_type.
-   **The Goal:** This makes it easy to group and aggregate. It calculates the **average** and **total** for every stat type per player and identifies which category a player was "strongest" in for each game.

**4. The Visualization (The Facet Grid)**

Finally, it uses **Seaborn** to create a grid of bar charts.

-   **Structure:** It creates a "FacetGrid" where each **row** is a different Player and each **column** is a different Game.
-   **The Bars:** Each mini-chart shows the player's FGM, FG3M, and FTM for that specific game.
-   **Cleanup:** It rotates the labels 45 degrees so they don't overlap and saves the whole thing as a high-res PNG (faceted_bar_chart.png).
