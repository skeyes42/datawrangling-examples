## SimpleJoinBoxscores.py

This Python program retrieves and integrates basketball data from an SQLite database using the **pandas** library. It follows a classic data science pipeline: connecting to a source, extracting raw tables, cleaning and merging them into a human-readable format, and finally sorting and refining the output.

**1. Database Connection and Extraction**

**Path Configuration:** The script identifies the database file Boxscores.db by looking at an environment variable called EXAMPLES.

**sqlite3.connect**: Establishes a formal connection to the database.

**Data Retrieval**: It uses pd.read_sql_query to pull three distinct tables directly into pandas DataFrames: Boxscores, Players, and Teams.

**2. Data Preparation**

**Column Renaming**: The script renames PLAYER_NAME to Player and TEAM_NAME to Team. This improves readability for the final output and ensures the merged columns have clear, user-friendly labels.

**3. Database-Style Joins (The Core Logic)**

The most critical part of the script is the **chained merge** operation. It uses a "Left Join" approach to enrich the core statistical data:

**Enriching Boxscores**: It takes the raw stats from the Boxscores table and "attaches" the player names from the Players table by matching their unique PLAYER_ID.

**Adding Team Info**: It then performs a second merge to attach the team names from the Teams table by matching the TEAM_ID.

**Result**: This transforms a table of IDs (e.g., "P101", "T05") into a table with actual names (e.g., "LeBron James", "Lakers").

**4. Final Refinement**

**Sorting**: The sort_values method organizes the results sequentially by GAME_ID and then by TEAM_ID, ensuring the output is ordered logically for a game-by-game review.

**Column Cleanup**: It uses .drop to remove the original PLAYER_ID and TEAM_ID columns. Since the descriptive names are now present, these technical IDs are no longer needed.

**Resource Management**: Finally, con.close() is called to properly disconnect from the database, a best practice for managing system resources in 2026.

**Why this approach?**

By performing these joins in **pandas** rather than raw **SQL**, the script gains flexibility for further Python-based analysis or visualization that might be harder to achieve within a standard database query.
