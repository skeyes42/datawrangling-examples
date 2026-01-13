## AnonymousFunctions.R

This R program is a data analysis script that retrieves basketball statistics from a local SQLite database and provides an interactive menu for the user to view summaries, tables, or visualizations.

**1. Data Retrieval (getBoxscores)**

The program defines a function to connect to a specific database (Boxscores.db).

**Database Connection:** It uses the DBI and RSQLite libraries to open a connection to the file path provided.

**Querying:** It uses dplyr (via tbl()) to point to the "Boxscores" table and collect() to pull that data from the database into a standard R data frame (df).

**Cleanup:** It safely disconnects from the database once the data is loaded into memory.

**2. Interactive Menu**

The script uses cat() and readline() to create a simple command-line interface. It asks the user to input "1", "2", or "3" to decide what to do with the basketball data.

**3. User Options (The Logic)**

**Option 1: View Means**

If the user selects **1**, the script calculates the average performance per game per team.

It groups the data by GAME_ID and TEAM_ID.

It calculates the **mean** for three specific columns: FGM (Field Goals Made), FG3M (Three-Pointers Made), and FTM (Free Throws Made).

**Option 2: View Boxscores Table**

If the user selects **2**, the script creates a calculated column called SCORING_EFFORT.

**Calculation:** It sums FGM, FG3M, and FTM for every row.

**Display:** It uses rhandsontable, which renders the data as an interactive, Excel-like spreadsheet in the RStudio Viewer.

**Option 3: Plot**

If the user selects **3**, the script generates a statistical visualization using ggplot2.

**Logic:** It calculates the same SCORING_EFFORT used in Option 2.

**Visualization:** It creates a **Boxplot** comparing "Scoring Effort" against the game outcome (WIN_LOSS). This allows a user to see if higher scoring efforts correlate with winning games.
