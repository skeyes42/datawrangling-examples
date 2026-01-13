## ReimagineBoxscoresAsOO.py

This Python program uses **object-oriented programming (OOP)** and **data classes** to structure basketball game data, moving from a flat, table-based format (using pandas DataFrames) into nested, interconnected objects (Player, Team, Game).

The primary purpose is to demonstrate how to **model real-world data relationships** in a structured way and then perform analysis on that structured data.

Here is a breakdown of the code's main sections:

**1. Imports**

The program imports necessary libraries:

dataclasses for easily creating classes that primarily store data.

typing.List for type hinting.

datetime.date for handling dates.

pandas for data manipulation, primarily for loading and analyzing data in tabular format.

**2. Data Classes (Player, Team, Game)**

This section defines the core data structures using the @dataclass decorator:

**Player**: Stores individual statistics for one player in a single game (minutes, points, rebounds, etc.).

It includes a \__post_init_\_ method to validate that minutes and points are non-negative.

The \__repr_\_ method provides a clean string representation when the object is printed.

**Team**: Represents one team's performance in a game.

It contains a list of Player objects (players: List[Player]).

In its \__post_init_\_ method, it automatically calculates the total_points by summing the points of all players on that team's roster.

**Game**: Represents a complete matchup.

It holds two Team objects (home_team, away_team).

In its \__post_init_\_ method, it automatically sets the home_score and away_score based on the teams' total points.

**3. Helper Function (create_game_from_boxscore)**

This function is crucial for translating data between formats:

It takes a flat pandas DataFrame (which resembles a single spreadsheet table) and a specific game_id.

It filters the DataFrame for that game, separates the data by team, creates Player objects for each roster, then wraps them into Team objects, and finally combines everything into a single Game object.

This process is called **Object-Oriented (OO) structure creation** or data hydration.

**4. Example Data Function (create_sample_data)**

This function generates a sample pandas DataFrame containing mock basketball statistics for a game between the Lakers and the Warriors. This provides the raw input data needed to run the program.

**5. Main Execution (main)**

This function orchestrates the entire process:

**Creation:** It calls create_sample_data() to get a DataFrame, then uses create_game_from_boxscore() to convert that DataFrame into the structured Game object.

**Display:** It prints a summary of the game, including the final score and individual player stats, using the custom \__repr_\_ methods.

**Analysis Examples:** It demonstrates two types of analysis on the *structured objects*:

It converts the list of Player objects back into a temporary pandas DataFrame to easily sort and display the top 3 scorers.

It calculates team shooting percentages using direct access to the attributes of the Player and Team objects within the game structure.

**In Summary**

The program demonstrates a powerful workflow:  
**Flat Data (DataFrame) → Structured Objects (Classes) → Analysis and Presentation.**  
This approach makes managing and analyzing complex, related data points much cleaner and more maintainable than working with flat tables alone.
