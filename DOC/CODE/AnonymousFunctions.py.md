## AnonymousFunctions.py

This Python program is an interactive data analysis tool that retrieves basketball statistics from a SQLite database and allows the user to choose between three different types of analysis.

As of 2026, it follows standard data science practices using the Pandas library for manipulation and Seaborn for visualization.

**1. Data Retrieval**

The program begins by defining a function get_boxscores() that:

Connects to Boxscores.db (located via the EXAMPLES environment variable).

Retrieves all columns and rows from the Boxscores table.

Returns the data as a Pandas DataFrame.

**2. User Interface**

The script prompts the user to enter a number (**1, 2, or 3**) to determine which analysis to run.

**3. Analysis Options**

**Option 1: View Means**

**Action:** Groups the data by GAME_ID and TEAM_ID.

**Calculation:** Calculates the average (mean) for Field Goals Made (FGM), Three-Pointers Made (FG3M), and Free Throws Made (FTM).

**Use Case:** Useful for seeing average team performance per game.

**Option 2: View Boxscores table (Scoring Effort)**

**Action:** Creates a new column called SCORING_EFFORT.

**Calculation:** Uses a lambda function to sum FGM + FG3M + FTM for every row.

**Use Case:** Provides a custom metric to see total scoring contributions per player/entry.

**Option 3: Plot (Visual Analysis)**

**Action:** Calculates the same SCORING_EFFORT metric from Option 2.

**Visualization:** Generates a **Boxplot** using Seaborn.

**Analysis:** Compares "Scoring Effort" against the game outcome (WIN_LOSS).

**Output:** A window opens showing the distribution (median, quartiles, and outliers) of scoring effort for winning games versus losing games.

**4. Technical Details**

**Matplotlib/Seaborn:** The plotting section uses plt.style.use('seaborn-v0_8-whitegrid') to ensure a clean, modern aesthetic.

**Clean-up:** The database connection is closed immediately after the data is retrieved to save system resources.
