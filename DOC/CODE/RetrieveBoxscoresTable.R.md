## RetrieveBoxscoresTable.R

This R program connects to an **SQLite database**, retrieves all records from a table called Boxscores, displays the data, and saves it as a CSV file. It is built with robust error handling to manage issues like missing database files or connection failures.

**1. Libraries and Setup**

The program uses four key libraries:

**RSQLite** & **DBI**: Provide the connection engine and interface to the SQLite database.

**dplyr**: Allows you to interact with the database using R syntax rather than writing raw SQL.

**readr**: Provides the write_csv function for fast file export.

It determines the database location by looking for an environment variable named EXAMPLES.

**2. Connection and Safety Checks**

The code is wrapped in a **tryCatch()** block, which prevents the program from crashing if an error occurs.

**File Verification**: It first checks if the database file exists at the expected path.

**dbConnect()**: Establishes a formal link between the R session and the .db file.

**3. The Database Query (Lazy Evaluation)**

The program uses a **"lazy"** approach to data retrieval:

**tbl(con, "Boxscores")**: Creates a reference to the table without actually pulling any data into R yet.

**show_query()**: Displays the actual SQL command (e.g., SELECT \* FROM Boxscores) that R has generated behind the scenes.

**collect()**: This is the "trigger" that tells R to actually run the query and download the results from the database into R's memory as a data frame.

**4. Output and Cleanup**

Once the data is successfully retrieved:

**dbDisconnect()**: Closes the connection to free up system resources like memory and sockets.

**write_csv()**: Exports the data to a local file named BoxscoresTable_Full.csv.

**Printing**: Displays the results in the console for immediate review.

**5. Error Handling**

If anything fails (e.g., the database is missing), the error function triggers, printing a specific error message and ensuring the database connection is safely closed even in a failed state.
