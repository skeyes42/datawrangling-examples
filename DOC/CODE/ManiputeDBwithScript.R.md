## ManiputeDBwithScript.R

This R program is a **database rebuild script**. It is designed to perform a "hard reset" of a sports database by deleting existing structures, recreating them from official blueprints (SQL files), and then repopulating them with fresh data from CSV files.

As of 2026, this modular approach is a standard way to ensure a data environment is clean and reproducible for analysis.

**1. Core Utility Functions**

The program defines two specialized tools to handle the heavy lifting:

**execute_script(con, script_name)**: This function acts as a bridge between R and SQL. It reads a .sql text file (like a "blueprint"), converts it into a single long string of commands, and uses dbExecute() to run those commands on the database. This is used for structural changes like DROP and CREATE.

**load_table(con, table_name, path_to_csv_file)**: This function handles the data injection. It uses readr::read_csv() to quickly pull data from a file into R and then uses dbAppendTable() to push that data into the specified database table.

**2. The Rebuild Workflow**

The main body of the script follows a strict "Destruction to Creation" sequence:

**Destruction**: It calls three separate "drop" scripts to delete the Boxscores, Players, and Teams tables. This wipes out all old or corrupted data.

**Creation**: It executes three "create" scripts to build brand-new, empty table structures with the correct column names and data types (e.g., setting PTS as an integer).

**Ingestion**: It reloads the database by pulling fresh data from three CSV source files: boxscores.csv, player_id.csv, and team_id.csv.

**3. Verification and Cleanup**

**dbListTables(con)**: After the process is finished, it prints a list of all tables currently in the database to verify that Boxscores, Players, and Teams were successfully recreated.

**dbDisconnect(con)**: It safely closes the connection to Boxscores.db. This is vital in 2026 to prevent file locking, which would stop other software (like a visualization dashboard) from accessing the data.

**Summary of Utility**

This script is a **Data Refresh Pipeline**. Instead of manually editing a database, an analyst runs this script to guarantee that their 2026 data environment is exactly the same every time they start a new project. It transforms raw text files into a high-performance relational database.
