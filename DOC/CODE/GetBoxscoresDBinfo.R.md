## GetBoxscoresDBinfo.R

This R program is a **database schema inspection tool**. Its primary purpose is to help a developer or analyst understand the internal structure of a SQLite database—specifically, what tables exist and what columns are inside them.

**1. Discovery Phase: Listing Tables**

The program first identifies the database file via the EXAMPLES environment variable and connects to it using the [DBI](https://dbi.r-dbi.org/) package.

**dbListTables(con)**: This is a high-level function that automatically queries the database to find all user-created tables.

**Result**: It prints a character vector of names, such as [1] "Boxscores" "Players" "Teams".

**2. Deep Inspection: Metadata Retrieval**

Once the tables are known, the script focuses on the **"Boxscores"** table to look "under the hood" at its configuration:

**PRAGMA table_info()**: This is a specialized SQLite command (called a Pragma) that returns a detailed report on a table's columns.

**dbGetQuery()**: This function executes the command and immediately returns the result as a standard R data frame.

**3. Understanding the Output**

The column_info data frame that is printed contains several critical metadata fields for every column in the table:

**cid**: The Column ID (its index/order in the table).

**name**: The name of the stat or field (e.g., GAME_ID, PTS).

**type**: The data format stored (e.g., INTEGER for whole numbers, TEXT for names, REAL for decimals).

**notnull**: A flag (0 or 1) indicating if the column is allowed to be empty.

**dflt_value**: The default value if no data is entered.

**pk**: A flag (0 or 1) identifying if the column is the **Primary Key** (the unique record identifier).

**4. Cleanup**

**dbDisconnect(con)**: This ensures the connection is severed safely, preventing the database file from remaining "locked" to other applications in 2026.

**Summary**

This script is a **diagnostic utility**. Before writing complex data science or visualization code, analysts use this to verify exactly what data types they are working with and to ensure they have the correct column names for their queries. [1]
