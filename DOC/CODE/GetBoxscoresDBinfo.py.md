## GetBoxscoresDBinfo.py

This Python program is a database inspection tool. It is used to discover the structure of an SQLite database by listing all available tables and then detailing every column within a specific table.

**1. Core Discovery Phase**

The program first connects to the Boxscores.db file and performs a "master inventory" check:

**Targeting the Master Table**: It queries sqlite_master, a hidden internal table that SQLite uses to store its own structure.

**Identifying Tables**: By filtering for type='table', it retrieves the names of every data table currently existing in the database.

**Result**: It prints a list of these names (e.g., ['Boxscores', 'Players', 'Teams']).

**2. Deep Inspection Phase (PRAGMA)**

Once it has the table names, it focuses on the **"Boxscores"** table to retrieve its "schema" (the blueprints of how the data is stored):

**PRAGMA table_info**: This is a special command that returns metadata about a specific table's columns.

**Column Metadata**: For every column in the table, it retrieves six key pieces of information:

**ID**: The numerical position of the column (starting at 0).

**Name**: The name of the column (e.g., GAME_ID, PTS).

**Type**: The data type (e.g., INTEGER, TEXT, REAL).

**NotNull**: A 1 (True) or 0 (False) indicating if the column requires a value.

**Default**: Any default value assigned to the column if left blank.

**PK**: A 1 (True) or 0 (False) indicating if this column is the **Primary Key** (the unique identifier for rows).

**3. Execution Flow**

**Connection**: It establishes a link to the database file found in the "EXAMPLES" environment folder.

**Cursor**: It creates a cursor object, which acts as the "pointer" to execute commands and fetch results.

**Output**: It formats the column information into a readable list of strings and prints them to the console for the developer to review.

**Cleanup**: It closes the connection to free up system memory and unlock the database file.

**Summary**

This is a **metadata exploration tool**. Analysts use it to understand what kind of data is available and how it is formatted before they begin writing complex data processing or machine learning scripts in 2026.
