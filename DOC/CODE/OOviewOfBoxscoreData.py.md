## OOviewOfBoxscoreData.py

This Python program is a **Data Modeling tool** that transforms raw database rows into a structured, hierarchical object model (often called Object-Relational Mapping or ORM). It is designed to represent the **2025/2026 basketball season** as a collection of nested Python objects.

**1. The Object Hierarchy (Data Classes)**

The program defines a four-level hierarchy using Python dataclasses:

**Player**: Stores individual stats (Field goals, 3-pointers, free throws).

**Team**: A collection of Player objects associated with a specific Team ID.

**Game**: A container for the two Team objects that competed against each other.

**Season2025**: The top-level container holding every Game object for the entire season.

**2. The Transformation Engine: load_season_from_db**

This function performs the heavy lifting by converting SQL tables into these Python objects:

**Extraction**: It connects to Boxscores.db and pulls all tables (Boxscores, Players, Teams, Season2025) into Pandas DataFrames.

**Iterative Mapping**: It loops through the data in three levels:

Finds unique **Games**.

Inside each game, finds unique **Teams**.

Inside each team, finds every **Player** and their specific stats.

**Instantiation**: As it loops, it "builds" the objects from the bottom up—creating Player objects, putting them into Team lists, putting those into Game objects, and finally into the Season object.

**3. Lookup Utilities**

The program includes two helper functions, get_player_name and get_team_name. These allow you to cross-reference the ID numbers found in your Season object with the descriptive names found in the reference tables (e.g., converting "ID 1610612738" to "Cleveland Cavaliers").

**4. Execution and Output**

The main() function serves as a demonstration of how an analyst would use this structured data in 2026:

It retrieves the database path from the EXAMPLES environment variable.

It loads the entire 2025 season into memory.

It demonstrates **deep access**: Instead of writing SQL, you can use Python dots to drill down, such as season.games[0].teams[0].players[0].

**Summary of Utility**

This program is much more powerful than a simple table viewer. It organizes data the way a person thinks about sports: **Season → Games → Teams → Players**. This makes it an ideal foundation for building complex 2026 sports simulations, fantasy sports engines, or advanced AI performance models.
