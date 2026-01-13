## BuildBoxscoresObject.py

This Python program is a data retrieval tool designed to extract sports statistics from a SQLite database and combine them into a single, readable Pandas DataFrame.

**1. Core Functionality: The Boxscores Class**

The class acts as a wrapper for database operations:

**\__init_\_**: Stores the file path to your SQLite database (Boxscores.db).

**boxscores_dataframe()**: This is the main engine of the program. It performs three key steps:

**Extraction**: It connects to the database and pulls data from three separate tables: Boxscores, Players, and Teams.

**Merging (Joining)**: It uses Pandas merge to perform "left joins." It links the raw boxscore stats to specific player names and team names using their ID numbers.

**Cleanup**: It removes the raw PLAYER_ID and TEAM_ID columns to make the final table cleaner, leaving only the descriptive information (like Names and Stats).

**2. Safety and Resource Management**

The program uses a **try...finally** block. This ensures that even if there is an error while reading the data, the connection to the database is always closed (con.close()), preventing memory leaks or file locking issues.

**3. Execution Flow (if \__name_\_ == "__main__":)**

When you run the script, it follows this sequence:

**Locates the File**: It looks for the database file in a folder defined by an environment variable named "EXAMPLES."

**Instantiates**: It creates an instance of the class via get_boxscores_instance.

**Processes**: It runs the merging logic and stores the final result in boxscores_data.

**Outputs**: It prints the final table (the merged data) to your console.

**Summary of the Result**

Instead of seeing three separate tables with confusing ID numbers, this program gives you one unified table where every game stat is clearly labeled with the correct **Player Name** and **Team Name**.
