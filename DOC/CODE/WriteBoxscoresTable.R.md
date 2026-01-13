## WriteBoxscoresTable.R

This R program demonstrates how to **initialize or reset a database table** by taking raw text data (CSV format) and saving it into an SQLite database as a structured table.

In 2026, this remains a standard "setup" or "data migration" script used to ensure a database has a consistent baseline of information. Here is the step-by-step explanation:

**1. Connecting to the Database**

**Pathing**: It uses Sys.getenv("EXAMPLES") to find the directory where your database should live and builds the path to Boxscores.db.

**dbConnect()**: This establishes the connection to the SQLite database. If the file doesn't exist yet, SQLite will create a new, empty file automatically [1].

**2. Processing the CSV Data**

**Raw Data**: The script defines a variable csv_Players_data containing a simple list of seven players (Fred, John, Trevor, etc.) and their IDs.

**read_csv()**: From the readr package, this function converts the text string into an R **data frame**.

**col_types**: It explicitly defines PLAYER_ID as an integer and PLAYER_NAME as a character (text) to ensure data integrity before it reaches the database [2].

**3. Writing to the Database**

**dbWriteTable()**: This is the core command that transfers the data from R's memory into the .db file.

**name = "Players"**: The table in the database will be named "Players".

**overwrite = TRUE**: This is a "reset" flag. If a table named "Players" already exists, it is deleted and replaced with this fresh data.

**row.names = FALSE**: This prevents R from adding an extra, unnecessary column of row numbers into your database [1].

**4. Verification and Cleanup**

**dbReadTable()**: To confirm the process worked, the script immediately reads the entire "Players" table back from the database into R and prints it.

**dbDisconnect()**: This is a critical step in 2026 to ensure the database file is unlocked and system resources (memory and file handles) are released [1].

**Summary of Results**

When you run this script, your Boxscores.db file will now contain a table named **Players** with exactly seven rows of data. This provides a clean starting point for other scripts to perform updates or joins.

| **PLAYER_ID** | **PLAYER_NAME** |
|---------------|-----------------|
| 1             | Fred            |
| 2             | John            |
