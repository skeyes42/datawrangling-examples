## ManiputeDBwithScript.py

This Python program is a **database administration script** designed to completely reset a SQLite database to a known, empty state. It uses the operating system's command line to execute SQL scripts, demonstrating a powerful way to manage database structure.

**1. Core Functionality: flush_database()**

The primary function automates the wiping and rebuilding of the database structure:

**Wiping Data**: It calls the external sqlite3 command-line tool and pipes the command .read drop_all_tables.sql into it. This SQL script contains commands like DROP TABLE IF EXISTS ... for every table, effectively deleting all data and the tables themselves.

**Rebuilding Structure**: It immediately follows up by executing the .read boxscores.sql script. This script contains CREATE TABLE ... commands, which restore the empty table structures, ready to accept new data.

**2. Execution via Subprocesses**

The program relies heavily on the subprocess.run() function:

**subprocess.run(...)**: This is how the Python script talks to the operating system's command line, just like you would run a command in your terminal. It executes the sqlite3 command-line application.

**check=True**: This is a critical safety feature. It tells Python to raise an error if the command-line operation fails (e.g., if the sqlite3 command isn't installed or the SQL file is missing), stopping the script safely.

**3. Verification and Demonstration**

The if \__name_\_ == "__main__": block serves as a demonstration and verification log:

**Setup**: It locates the scripts folder using the EXAMPLES environment variable.

**Initial Flush**: It calls the flush_database() function and prints the list of tables (before) to confirm the tables exist.

**Manual Demonstration**: It then repeats the drop and recreate steps manually, printing the table list after each step (after_dropping, after_recreating) to visually prove that the operations worked as expected.

**db_list_tables()**: This helper function connects directly to the database via Python and lists the current tables to monitor progress.

**Summary of Utility**

This script is essential for development and testing environments in 2026. Data scientists use it to reset their database to a pristine state before running a large data pipeline, ensuring that every run starts with clean data and produces consistent, reproducible results.
