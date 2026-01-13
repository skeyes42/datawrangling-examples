## SimpleJoinBoxscores.R

This R program performs a **database table join** and **data enrichment** task. It takes a raw basketball statistics table and merges it with descriptive information (Player and Team names) to create a more useful dataset.

In the context of **2026**, this script utilizes the dbplyr "lazy evaluation" workflow, which is the standard for efficient database management.

**1. Database Connection**

It locates the database Boxscores.db using the EXAMPLES environment variable.

dbConnect establishes the link between R and the SQLite database engine.

**2. Relational Joins (The Core Logic)**

The program uses a **chain of pipes (\|\>)** to build a complex query without actually writing raw SQL:

**tbl(con, "Boxscores")**: This starts with the central statistics table.

**left_join (Players)**: It looks at each player's ID and pulls in their name and details from the Players table.

**left_join (Teams)**: It looks at the team ID and pulls in the full team name from the Teams table.

**arrange**: It sorts the results logically by game and then by team.

**3. "Lazy" SQL Generation**

**show_query(query)**: This is a powerful feature. Because R is "lazy," it hasn't actually downloaded any data yet. This command shows the SQL code that R has automatically translated for the database (e.g., SELECT \* FROM Boxscores LEFT JOIN ...).

**4. Data Transfer and Update**

**collect()**: This is the "trigger" that tells R to actually execute the query and pull the final combined table into R's memory as a data frame.

**dbWriteTable**: This step is critical. It takes the new, enriched table (now containing names, not just IDs) and **overwrites** the original Boxscores table in the database (overwrite = TRUE).

**Cleanup**: The script closes the connection with dbDisconnect(con) to prevent memory leaks or file locking issues.

**5. Final Output**

The print(results_df, width = Inf) command displays the final table in the R console, showing all columns (stats, player names, and team names) across the full width of the screen.

**Summary for 2026**

This script transforms a database from "technical" (IDs only) to "human-readable" (Names + Stats). By overwriting the table, the program ensures that any other app or person opening Boxscores.db in the future will see the full, enriched data immediately. RSQLite Documentation \| dplyr Joins
