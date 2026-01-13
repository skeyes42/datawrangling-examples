## AccessClassDefsEnvVar.R

This R program demonstrates **object-oriented programming (OOP) principles** and modularity. It uses a custom-built "class" system to fetch basketball data from a database.

Here is the breakdown of each section:

**1. Environment and Path Setup**

**Sys.getenv("EXAMPLES")**: It retrieves a base directory path stored in your computer's environment variables.

**file.path()**: It constructs clean file paths for a library folder and the specific Boxscores.db database file. This ensures the code works on different operating systems (Windows vs. Mac/Linux).

**2. Loading the External Module**

**source(...)**: This is the R equivalent of an "import" statement. It reads and executes the script BoxscoresClass.R.

This external file contains the definitions for the functions used later, keeping the main script clean and allowing you to reuse the database logic in other projects.

**3. Instantiating the Data Object**

**get_Boxscores_instance(path_to_database)**: This function acts as a **constructor**. It creates a specific "object" (stored in boxscoresObject) that contains the connection details to the database.

By passing the path here, you are telling the object exactly which database file it should "talk" to.

**4. Retrieving the Data**

**boxscores_dataframe(boxscoresObject)**: This is a method (or helper function) that interacts with the boxscoresObject.

It handles the heavy lifting: opening the connection, running a SQL query (like SELECT \* FROM Boxscores), converting the results into a standard R **data frame**, and then likely closing the connection automatically.

**5. Output**

**print(boxscores_df)**: Finally, it displays the full table of basketball box scores (player stats, points, etc.) in the R console.

**Why use this approach?**  
Instead of writing complex SQL code directly in your analysis, this program uses an **abstraction layer**. If the database structure changes in the future, you only have to update the BoxscoresClass.R file, and this main script will still work perfectly.
