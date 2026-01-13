## UpdatePlayersTable.R

This R program connects to an SQLite database and performs a targeted **data modification** to update a specific record in the Players table.

It follows a standard 2026 database workflow using the DBI and RSQLite libraries. Here is the step-by-step explanation:

**1. Database Connection**

**Pathing**: It builds the file path to Boxscores.db using the EXAMPLES environment variable.

**dbConnect()**: Establishes a formal link between the R session and the SQLite database file.

**2. The SQL UPDATE Operation**

The core of the program is the SQL string:  
UPDATE Players SET PLAYER_NAME = 'Johnie' WHERE PLAYER_ID = 2;

**UPDATE**: Tells the database to modify existing data.

**SET**: Specifies the new value ('Johnie') for the PLAYER_NAME column.

**WHERE**: Provides a critical filter. It ensures only the player with the unique ID of 2 is updated. Without this clause, every player in the database would be renamed "Johnie."

**dbExecute()**: Unlike dbGetQuery() (which is for retrieving data), dbExecute() is specifically designed for operations that **change** the database (like updates, deletes, or inserts). It returns the number of rows affected.

**3. Verification and Cleanup**

**dbReadTable()**: This function pulls the entire updated Players table into R as a data frame. This allows you to immediately verify that the change was successful in the console.

**dbDisconnect()**: A best practice in 2026 to ensure the database file is unlocked and system resources are released.

**Summary of Result**

When run, the program permanently changes the name of the player with ID 2 to "Johnie" in the .db file, prints the updated list of players to the R console, and closes the connection.

For more information on these functions, you can refer to the DBI Package Documentation and the RSQLite Package Documentation.
