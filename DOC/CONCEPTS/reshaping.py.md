## reshaping.py

Here's how it translates the workflow into Python:

**1. The Database Connection (SQLite + SQL Query)**

The script uses Python's built-in sqlite3 library to connect to the same Boxscores.db file.

-   **pd.read_sql_query**: This is a powerful pandas function. Instead of manually writing R-style joins (left_join), the Python script uses a raw **SQL query** to join the Boxscores, Players, and Teams tables directly within the database.
-   **Efficiency**: This method is efficient because the complex merging happens inside the fast SQLite database engine, before the data is loaded into Python's memory.

**2. The Data Reshaping (melt & pivot_table)**

The script uses pandas functions to replicate R's pivot_longer and pivot_wider logic:

-   **shooting.melt(...)**: This "melts" the data into a long format, stacking stats like FGM and FGA into a single count column, which is equivalent to R's pivot_longer.
-   **String Manipulation**: It uses Python's string accessors (.str[:-1] and .str[-1]) to split FGM into FG and M, just like R's separate function.
-   **shooting_long.pivot_table(...)**: This pivots the data again, bringing 'M' (Made) and 'A' (Attempted) back into side-by-side columns, ready for math.

**3. The Analytics (Shooting %)**

The final step is calculating the efficiency metrics:

-   **Calculation**: A new pct column is created using simple arithmetic (M / A \* 100).
-   **groupby().agg(...)**: This is pandas' robust way of summarizing data. It groups the data by player name and shot type and calculates the total attempts and the average shooting percentage.

**Key Tools & Links:**

-   **Pandas Melt**: The equivalent of R's pivot_longer.
-   **Pandas Pivot Table**: A flexible way to reshape and aggregate data, similar to pivot_wider and group_by in R.
-   **Python SQLite3 Docs**: The built-in library for database interaction.

**In summary:** This Python script uses highly optimized pandas methods to perform the exact same professional data analysis workflow seen in the previous R script.
