## FlatvsOO.py

This program demonstrates how to transform

**flat, tabular data** (a pandas DataFrame) into a **hierarchical object structure** using Python **dataclasses**.

In 2026, this pattern remains a standard way to bridge the gap between "relational" data (rows and columns) and "domain-driven" modeling (objects that mirror real-world relationships).

**1. Data Structure Setup**

The script begins with a standard pandas DataFrame. This is **relational**; every row repeats the GAME_ID and TEAM_ID. While great for computation, it doesn't explicitly show that a "Game" is a single entity containing multiple "Players."

**2. Defining the Hierarchy (@dataclass)**

The program uses the dataclasses module to define three levels of data nesting:

**Player**: The leaf node, containing individual stats.

**Game**: A container holding a unique ID and a **List** of Player objects.

**Season**: The root container holding a **List** of Game objects.

**3. The Transformation Logic (build_season)**

The build_season function acts as a "parser" to restructure the data:

**Grouping**: It identifies unique games using .unique().

**Mapping**: For each game, it filters the rows and uses a **list comprehension** to instantiate Player objects for every row in that specific game.

**Nesting**: It bundles those players into a Game object and appends them to a Season.

**4. Comparison of Access Methods**

The program contrasts two ways to retrieve the same piece of information:

**Flat/Relational Access**: Uses pandas filtering logic: df[(df['GAME_ID'] == 1000) & ...]. This requires specific knowledge of the table's column names and filtering syntax.

**Hierarchical/OO Access**: Uses "dot notation" to traverse the objects: season.games[0].players[0].fgm. This is often more intuitive for developers building applications or APIs, as the data structure itself explains the relationships.

**Summary of Key Features**

| **Feature**       | **Relational (Pandas)**    | **Object-Oriented (Dataclasses)** |
|-------------------|----------------------------|-----------------------------------|
| **Logic**         | Vectorized / Set-based     | Instance-based / Traversal        |
| **Type Safety**   | Implicit (Dynamic)         | Explicit (via Type Hints)         |
| **Best Use Case** | Data Analysis & Statistics | Application Logic & Model Design  |

By converting the data to a Season object, you create a structure that is easier to pass into functions that only care about a specific Game or Player without carrying around the overhead of the entire original table.
