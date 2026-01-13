## RetrieveSeason2025Table.R

This R program connects to an SQLite database specifically to retrieve basketball data from the **Season2025** table. It uses a modern R workflow that allows you to treat a database table as if it were a local data frame.

Here is a succinct breakdown of the program's logic for 2026:

**1. Database Connection and Safety**

The program dynamically builds the file path using the EXAMPLES environment variable. Before attempting a connection, it performs a **pre-flight check** using file.exists(). This prevents the program from hanging or creating an empty dummy database file, which is a common default behavior of SQLite when a path is not found.

**2. DBI and dbplyr Integration**

The program utilizes the dbplyr interface (via tbl()) to interact with the database:

**tbl(con, "Season2025")**: Instead of writing a raw SQL string like "SELECT \* FROM...", it creates a pointer to the **Season2025** table.

**Lazy Evaluation**: The command select(everything()) describes what data you want, but R does not actually download the data yet.

**show_query()**: This is a debugging tool that prints the translation of your R code into the SQL code that will actually run on the database engine.

**3. Execution and Data Transfer**

**collect()**: This is the most critical step. It executes the SQL query on the database and transfers the results into your computer's RAM as a standard R data frame (results_df).

**Resource Management**: Immediately after collecting the data, the program calls dbDisconnect(con). This is a best practice in 2026 to ensure database locks are released and memory is managed efficiently.

**4. Robust Error Handling**

The entire process is wrapped in a tryCatch block. If the table Season2025 is missing or the database file is corrupted:

The program catches the error.

It prints a detailed diagnostic message including the attempted file path.

**Safety Cleanup**: It includes a specific check (dbIsValid) to ensure the connection is closed even if the program fails halfway through, preventing "leaked" connections.

**5. Expected Output**

When run, the program will:

Print the generated SQL code.

Print the full width of the **Season2025** dataset (columns typically include game_id, player_name, points, etc.).

Confirm completion with "Done".
