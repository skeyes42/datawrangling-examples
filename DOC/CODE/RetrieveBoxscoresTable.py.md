## RetrieveBoxscoresTable.py

This Python program retrieves all data from a specific table within an **SQLite database** and displays it as a formatted table using the **pandas** library.

**Core Components**

**Database Connection:**

It locates a database file named Boxscores.db by looking up an environment variable called EXAMPLES.

It uses a **context manager** (with sqlite3.connect(...)) to establish the connection. This is a best practice because it ensures the database connection is managed safely, though you typically still need to close it manually for complete resource cleanup in some environments.

**Data Retrieval with Pandas:**

The core command is pd.read_sql(query_text, con).

This single line replaces multiple manual steps (creating a cursor, executing a query, and fetching rows) by directly converting the SQL result into a **pandas DataFrame**.

The SQL query SELECT \* FROM Boxscores tells the database to "get every column and every row from the Boxscores table."

**Error Handling:**

The entire process is wrapped in a try...except block to catch sqlite3.Error. If the file is missing, the table doesn't exist, or the path is incorrect, the program will print a descriptive error message instead of crashing.

**What the Output Looks Like**

When executed, the program prints:

**Executing query:** A confirmation of the SQL being run.

**The Table:** A structured view of the Boxscores data, including column headers and row indexes.

**Done:** A final status message.

**Prerequisites for 2026**

For this to run successfully today in 2026, ensure:

An environment variable EXAMPLES is set on your system pointing to the directory containing your database.

The Boxscores.db file actually contains a table named Boxscores.

You have the pandas and sqlite3 libraries installed (sqlite3 is built into Python).
