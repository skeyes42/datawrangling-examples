## FunctionToAccessBoxscores.R

This R program is a straightforward data utility function designed to extract the complete contents of the "Boxscores" table from a SQLite database and load them into R's memory.

**1. Functional Structure: getBoxscores()**

The program is built around a single, reusable function that handles the entire lifecycle of a database request:

**Connection**: It uses the [DBI package](https://dbi.r-dbi.org/) and RSQLite to open a connection to the database file path provided as an argument.

**Query Building**: It uses dplyr syntax (tbl(con, "Boxscores") \|\> select(everything())) to point to the data. In 2026, this remains the preferred method because it is highly readable.

**Data Retrieval**: The collect() function is the "trigger" that tells R to actually execute the SQL command and download the data into a standard R data frame (tibble).

**Cleanup**: Crucially, the function calls dbDisconnect(con) before returning the results. This ensures the database file is not left "open," which prevents file locking and memory leaks.

**2. Execution Flow**

Outside of the function, the script performs the following steps:

**Path Configuration**: It retrieves a folder path from the system environment variable EXAMPLES and appends the filename Boxscores.db.

**Function Call**: It passes that path to the getBoxscores() function and stores the returned table in the variable df.

**Display**: It prints the table to the console and outputs "Done" to signify a successful run.

**Summary of Utility**

This script serves as a **clean data loader**. By wrapping the database logic inside a function, the developer has made it easy to import box score data into any larger 2026 analysis project without having to rewrite the connection and disconnection code every time.
