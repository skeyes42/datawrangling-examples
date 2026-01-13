## ComputePercentagesPoints.py

This Python program is a data pipeline designed to automate the calculation of basketball statistics (field goal percentages and total points) and update a database with the new results.

**1. Data Extraction**

**Database Location**: It finds the database path by looking at an environment variable named EXAMPLES. If that variable isn't set, it looks in the current folder.

**Connection**: It establishes a link to Boxscores.db using the standard sqlite3 library.

**Loading**: It reads the entire Boxscores table into a **Pandas DataFrame**, which is a powerful table structure used for data manipulation in 2026.

**2. Advanced Transformations**

The program uses a "chained" method approach (.assign()) to perform several calculations in sequence:

**Type Conversion**: It first ensures that shooting stats (FGM, FGA, etc.) are treated as **floats** (decimal numbers) so that divisions result in accurate percentages.

**Percentage Calculations**: It calculates Field Goal (FG), 3-Point (FG3), and Free Throw (FT) percentages. It uses np.where to safely handle cases where a player had 0 attempts, preventing a "division by zero" error by setting the percentage to 0 instead of NaN or inf.

**Point Totals**: It calculates points for each type of shot:

**2-pointers**: (FGM - FG3M) \* 2

**3-pointers**: FG3M \* 3

**Free Throws**: FTM \* 1

**Final Score**: It sums these together into a new PTS column and then sorts the table by Game and Team ID.

**3. Data Export and Cleanup**

**Database Update**: It uses to_sql with if_exists="replace" to **overwrite** the original Boxscores table in the database with the newly calculated data.

**CSV Backup**: It also saves the modified data to a file named results.csv.

**Resource Management**: It finally closes the database connection to free up system memory and prevent file locking.

**Summary of Results**

The end result is a modified **Boxscores** table that now contains calculated shooting percentages and total points for every entry, providing a complete statistical record for analysis.
