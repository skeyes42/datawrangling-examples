## BuildTeamsObject.R

This R program is a specialized data extractor designed to retrieve information from the **"Teams"** table of a SQLite database. It follows a professional, modular design using R’s modern **S7 object-oriented system**.

**1. Object-Oriented Design (S7)**

The program uses the S7 package to create a structured "Teams" object:

**new_class**: Defines the "Teams" blueprint, which holds a single property: the file path to the database.

**new_generic**: Creates the teams_dataframe command. In R, generics allow the same function name to behave differently depending on the object it is given.

**method(...) \<-**: Assigns the actual logic to the generic. It tells R: "When teams_dataframe is called on a Teams object, execute the database connection and retrieval."

**2. Efficient Database Handling**

The data retrieval is handled by the [DBI](https://dbi.r-dbi.org/) and dplyr packages:

**dbConnect**: Opens a secure connection to the Boxscores.db file.

**tbl(con, "Teams")**: Rather than loading the whole database, it creates a "lazy" reference specifically to the Teams table.

**collect()**: This is the execution step. It pulls the data from the database and converts it into a standard R data frame (tibble) that you can work with.

**dbDisconnect**: Ensures the connection is closed after the data is retrieved, which is a best practice to prevent file corruption or memory issues.

**3. Execution Flow**

**File Path**: It retrieves the folder location from a system environment variable called EXAMPLES and targets the file Boxscores.db.

**Instantiate**: It creates teams_object, an S7 object that "knows" where the data lives.

**Process**: It runs the teams_dataframe() method to fetch the team list (usually containing columns like TEAM_ID, TEAM_NAME, and ABBREVIATION).

**Output**: It prints the resulting table to the console.

**Summary**

This program provides a clean, reusable way to access team data. By wrapping the database logic inside an **S7 class**, the code is highly organized and can be easily integrated into larger sports analytics projects in 2026.
