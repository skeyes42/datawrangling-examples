## BuildBoxscoresObject.R

This R program performs the exact same task as the Python version you provided—merging sports database tables—but uses **R's functional programming style** and the modern **S7 object-oriented system**.

**1. The Object System (S7)**

The program uses the S7 package, which is the new successor to R's older S3 and S4 systems.

**new_class**: Defines a "Boxscores" object that stores the file path to the database.

**new_generic**: In R, methods (functions) are often separate from data. This creates a generic command called boxscores_dataframe.

**method(...) \<-**: This tells R: "When boxscores_dataframe is called on a Boxscores object, run this specific code."

**2. Efficient Data Handling (dplyr & dbplyr)**

Instead of pulling all data into memory immediately, this program uses dplyr and DBI to handle the database efficiently:

**tbl(con, "...")**: Creates a reference to the database tables without actually downloading the data yet.

**Lazy Joins**: The left_join and select commands are converted into SQL automatically by R. The actual merging happens **inside the database engine** (SQLite), which is much faster for large datasets.

**collect()**: This is the crucial step where the processed data is finally downloaded from the database into your R environment as a standard tibble/data frame.

**3. File Output and Management**

**dbDisconnect(con)**: Properly closes the database connection to prevent file corruption.

**sink("results.txt")**: Instead of just printing to the screen, this "redirects" the output. Everything that follows (the table data) is written directly into a text file named results.txt.

**Sys.getenv("EXAMPLES")**: Dynamically finds the database file location based on your computer's environment settings.

**Summary of Difference from Python**

While the Python version used **Pandas** to merge data *after* loading it, this R version uses **dplyr** to tell the **Database** to do the merging before the data even reaches R. The result is the same: a clean table with Player and Team names instead of ID numbers.
