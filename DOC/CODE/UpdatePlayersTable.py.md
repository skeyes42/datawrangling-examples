## UpdatePlayersTable.py

This Python program connects to an SQLite database and performs a **data modification** operation, specifically updating a player's name within the Players table. It demonstrates how to execute SQL commands that alter data stored in a database file.

**1. Database Connection (Context Manager)**

The script first connects to the Boxscores.db file. It uses a **context manager** (with sqlite3.connect(...) as con:). In 2026, this is standard Python practice because it automatically handles closing the connection, even if errors occur, ensuring efficient resource management.

**2. The SQL UPDATE Command**

The core function is the SQL UPDATE statement:

sql

UPDATE Players

SET PLAYER_NAME = 'Johnie'

WHERE PLAYER_ID = 2;

Use code with caution.

**UPDATE Players**: Specifies the table where changes will be made.

**SET PLAYER_NAME = 'Johnie'**: Defines the new value for the PLAYER_NAME column.

**WHERE PLAYER_ID = 2**: This is a crucial filter. It ensures that *only* the row where the PLAYER_ID matches 2 is changed, preventing all players in the table from being renamed "Johnie".

**3. Execution and Commitment**

**cur.execute(sql_update_query)**: This sends the update instruction to the database engine.

**con.commit()**: This is vital for UPDATE, INSERT, or DELETE operations. It permanently saves the changes to the disk file. Without this line, the change would only exist temporarily in the active memory session and would be lost when the program ends.

**4. Verification**

After the update, the script uses pandas.read_sql_query to instantly read the entire updated Players table back into a DataFrame. This allows the user to immediately see that the row for PLAYER_ID = 2 now has the name "Johnie".

**Summary for 2026**

This script is a robust example of targeted data manipulation. It shows how to safely alter specific records in a production database environment and confirm the changes using modern data science libraries (pandas).
