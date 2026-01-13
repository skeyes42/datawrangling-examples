## reshaping.R

This program takes the concepts from the previous scripts and applies them to a **real-world database environment**. Instead of building data from scratch, it pulls information from a SQL database and performs more advanced "feature engineering" to calculate shooting percentages.

Here is the breakdown for January 2026:

**1. The Database Connection**

The script uses RSQLite to connect to a local database file (Boxscores.db).

-   **The Join:** It uses left_join to merge three different tables (**Boxscores**, **Players**, and **Teams**).
-   **The Logic:** This replaces ID numbers (like 101) with actual names (like "Stephen Curry"), making the data human-readable before it even leaves the database.
-   **collect():** This is a crucial step. It tells R to execute the SQL query and bring the results into your computer's memory as a "tibble" (a modern data frame).

**2. The Data Reshaping (Pivot & Separate)**

This is the clever part of the script. It needs to calculate percentages, but the data is messy.

-   **pivot_longer**: It stacks all shot stats (FGM, FGA, etc.) into one column.
-   **separate**: It splits strings like FGM into two pieces: FG (the shot type) and M (the outcome: Made). This allows the computer to understand that "FGM" and "FGA" are related to the same thing.
-   **pivot_wider**: It puts "Made" (M) and "Attempted" (A) into side-by-side columns.

**3. The Analytics (Shooting %)**

Now that it has "M" and "A" for every shot type, it performs the math:

-   **Calculation**: It creates a pct column (Made / Attempted \* 100).
-   **Summarization**: It groups by player and shot type to show their **total volume** (how many shots they took) and their **efficiency** (how often they went in).

**Key Tools & Links:**

-   **dbplyr**: This is working behind the scenes. It translates your R code into SQL so the database can understand it.
-   **RSQLite**: The bridge that connects R to the SQLite database engine.
-   **Tidyverse Separate**: Used here to elegantly split column names into usable categories.

**In short:** It moves from "What happened in this game?" to "How good of a shooter is this person overall?" by connecting to a professional database.
