## FlatvsOO.R

This R program demonstrates how to transform flat, relational data (a standard data frame) into a complex, **hierarchical object structure** using the modern **S7 object-oriented programming system**.

The goal is to move from data stored in rows and columns to data nested inside meaningful, related objects.

**1. Data Initialization**

A standard tibble (data frame) is created. This format is "flat," meaning every single observation (a player's stats in a single game) gets its own row.

**2. Defining the Hierarchy with S7**

Three S7 classes are defined to mirror real-world relationships:

**Player**: A simple container for a player's ID and stats (fgm, fg3m, ftm).

**Game**: Contains a game_id and, crucially, a class_list property named players. This list holds multiple Player objects.

**Season**: The top-level container that holds a class_list property named games. This list holds multiple Game objects.

**3. The Transformation Function (build_season)**

This is the core logic that manually reconstructs the hierarchy:

It iterates through each unique GAME_ID.

For each game, it iterates through the players in that game.

It creates a Player S7 object for each row.

It collects all Player objects into a list, then wraps them in a Game S7 object.

Finally, it collects all Game objects into a single Season S7 object.

**4. Demonstrating Access Methods**

The program contrasts the two ways to access the data:

**Flat Access:** Requires complex filtering logic to find a specific data point: df\$FGM[df\$GAME_ID == 1000 & df\$PLAYER_ID == 1].

**Hierarchical Access:** Uses object properties and list indices to navigate the structure, which mirrors the data's natural relationship: season@games[[1]]@players[[1]]@fgm.

**Summary**

This approach moves away from standard data frame manipulation toward strict, type-safe object modeling. This pattern is powerful for applications where the relationships between data points (e.g., a Season *has* Games, which *have* Players) are more important than simple tabular analysis.
