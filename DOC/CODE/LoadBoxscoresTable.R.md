## LoadBoxscoresTable.R

This R program is a **data ingestion pipeline** designed to transfer information from a flat CSV file into a structured SQLite database.

As of 2026, using the combination of readr for fast file reading and DBI for database management is the standard professional approach for this task.

**1. Resource Setup**

The program first defines where the files are located using the Sys.getenv and file.path functions:

**Dynamic Paths**: It looks for a folder specified in the system's "EXAMPLES" environment variable.

**Target Files**: It prepares references for the source file (boxscores.csv) and the destination database (boxscores.db).

**2. The Data Transfer Process**

The script follows a simple three-step workflow:

**Reading**: It uses readr::read_csv() to load the box score data into R. The setting show_col_types = FALSE is used to keep the console output clean by hiding the automatic data type detection message.

**Connecting**: It establishes a link to the database using DBI::dbConnect().

**Appending**: It uses dbAppendTable() to add the new data to the bottom of the existing "Boxscores" table. Unlike "overwriting," this preserves the data that was already in the database.

**3. Clean Exit and Verification**

**dbDisconnect()**: This is a critical step that safely closes the connection. It prevents the database file from becoming corrupted or staying "locked" by R, which would stop other programs from using it.

**Verification**: Finally, it prints the loaded data to the console so the user can verify the contents before the program outputs "Done."

**Summary of Utility**

This script acts as a **data bridge**. It is commonly used in sports analytics to take raw daily game data (often exported from websites as CSVs) and store it permanently in a centralized database for long-term tracking and analysis.
