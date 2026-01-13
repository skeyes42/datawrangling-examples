## ComputePercentagesPoints.R

This R program is a powerful data processing script that uses the **dplyr** and **DBI** packages to calculate basketball statistics directly within a SQLite database file and save the results.

**1. The Core Philosophy: "Lazy Evaluation"**

The most important feature of this R program is that it uses *lazy evaluation*. The commands you see (like mutate, select, arrange) are not executed in R itself; instead, R translates these into a single, complex **SQL query** that runs directly on the database engine. This is highly efficient for very large databases.

**2. The Workflow**

The script follows these main steps:

**Connection**: It connects to the Boxscores.db file using dbConnect.

**Query Building**: A sequence of operations builds the logic:

**Type Conversion**: Ensures the raw statistical columns are treated as decimal numbers (as.double).

**Calculation (mutate)**: It adds several new columns:

**Percentages**: It uses R's case_when to calculate shooting percentages (FG_PCT, FG3_PCT, FT_PCT), carefully handling division by zero cases by setting the percentage to 0 if zero attempts were made.

**Points**: It calculates two-pointer points, three-pointer points, and free-throw points, summing them up for a total PTS column.

**Cleanup (select, arrange)**: It sorts the results by Game and Team ID and removes the temporary point-calculation columns (FG2_PTS, etc.).

**Execution**:

show_query(query): This prints the actual SQL code R generated to the console (e.g., SELECT ... WHERE ... code).

collect(): This is the moment the SQL query runs on the database, and the results are downloaded into an R data frame (results_df).

**3. Export and Cleanup**

**Database Update**: It overwrites the original Boxscores table in the database with the new, fully calculated data frame using dbWriteTable(..., overwrite = TRUE).

**CSV Output**: It saves the results to a separate file named simple_boxscores.csv.

**Disconnect**: It closes the database connection cleanly.

**Summary of Results**

The program efficiently processes raw box score data to add critical summary statistics (percentages and total points), updates the database file on disk, and provides a CSV backup of the final, enriched dataset.
