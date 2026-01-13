## reshaping1.R

This is the **R (Tidyverse)** version of the Python script you just showed me! It performs the exact same basketball data transformations but uses R's signature "pipe" (\|\>) syntax.

Here is the breakdown:

**1. The Setup (Tibble)**

Instead of a dictionary, it uses tibble::tribble() to build the dataset row-by-row. It’s the same 8 rows of player stats (FGM, FG3M, FTM).

**2. pivot_wider: Tracking Growth**

-   **The Move:** It stretches the data horizontally.
-   **The Result:** Each player gets one row, with columns like FGM_game1000 and FGM_game2000 sitting next to each other.
-   **The Goal:** It uses mutate() to create FGM_change, showing exactly how much a player improved (or declined) between the two games.

**3. pivot_longer: Stat Breakdown**

-   **The Move:** It collapses the three stat columns into a single "Stat Type" column.
-   **The Result:** The data gets "tall," making it easy to run calculations across all types of points.
-   **The Goal:** It calculates the mean() and sum() for every player’s stats and uses slice_max() to find the single best stat category for each player per game.

**4. The Visualization (ggplot2 + ggpattern)**

This is where the R version gets a bit more "fancy" than the Python version:

-   **The Grid:** facet_grid(PLAYER_ID \~ GAME_ID) creates the same layout (Players on the side, Games on top).
-   **The Textures:** It uses geom_col_pattern(). Unlike the plain gray bars in Python, this adds geometric patterns (stripes, dots, etc.) to the bars based on the stat type.
-   **The Polish:** It tilts the X-axis labels 45 degrees for readability and saves the result as a PNG.

**Key Tools Used:**

-   **dplyr:** For filtering, grouping, and calculating (mutate, summarize).
-   **tidyr:** For the pivoting magic (pivot_wider, pivot_longer).
-   **ggplot2:** The gold standard for R plotting.
-   **ggpattern:** A specialized library for adding patterns to charts (great for black-and-white printing!).
