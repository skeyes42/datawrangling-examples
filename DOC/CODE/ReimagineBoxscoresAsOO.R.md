## ReimagineBoxscoresAsOO.R

This R program performs **Object-Oriented Programming (OOP)** using the **S3 system** to organize basketball statistics. It takes "flat" data (a spreadsheet-style table) and converts it into a nested hierarchy of "objects": a **Game** that contains two **Teams**, each containing a list of **Players**.

Here is a breakdown of the components:

**1. Data Setup (tibble)**

The program begins by creating boxscore_data, a **tibble** (an enhanced data frame). It contains raw stats for 10 players (5 Lakers, 5 Warriors) for a single game (G001). This represents the kind of data you would typically download from a sports database.

**2. S3 Class Constructors**

In R’s S3 system, classes are created by building a list and setting its class attribute. The program defines three constructors:

**Player()**: Stores individual stats (points, rebounds, etc.).

**Team()**: Stores the team name and a list of Player objects.

**Game()**: Stores the game ID, date, and two Team objects.

**3. Data Transformation (create_game_object)**

This is the "engine" of the program. It uses **dplyr** functions (filter, rowwise, summarise) to:

Filter the table for a specific game_id.

Iterate through the rows to turn each row of stats into a Player object.

Group those players into their respective Team objects.

Package everything into a final Game object.

The use of list() inside summarise is a key technique in R for creating **list-columns**, allowing you to store complex objects directly inside a data frame before pulling them out.

**4. Custom Print Methods**

R allows you to define how an object appears in the console by creating a function named print.ClassName.

**print.Player**: Formats stats into a readable string (e.g., "LeBron James: 28 pts...").

**print.Team**: Prints the team header and then loops through the players, calling the print.Player method for each.

**print.Game**: Prints the game header and then calls the print.Team method for both teams.

By defining these, simply typing print(game) triggers a cascading "pretty-print" of the entire game's data.

**5. Accessing the Data**

The end of the script demonstrates how to navigate the nested structure using the \$ and [[ ]] operators:

game\$home_team\$name gets the team name.

game\$home_team\$players[[1]]\$points digs three layers deep to find the points scored by the first player on the home team.

**Why do this?**

While a data frame is great for calculations (like average points), this **Object-Oriented** approach is better for:

**Organization:** It keeps related data (like a team name and its players) physically bundled together.

**Readability:** It allows you to use print(game) and see a structured report rather than a messy table.

**Scalability:** You could easily add "methods" to calculate things like is_winner(game) or get_top_scorer(team) that belong specifically to those objec
