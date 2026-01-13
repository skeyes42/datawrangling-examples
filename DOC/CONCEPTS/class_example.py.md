## class_example.py

This Python program demonstrates **Object-Oriented Programming (OOP)** by wrapping a pandas DataFrame inside a custom class. This is a common design pattern used to enforce data integrity and provide specialized behavior for specific datasets.

**1. The Boxscore Class**

The class acts as a "container" for basketball statistics with the following features:

**Initialization (__init__)**: When you create a Boxscore object, it stores the DataFrame and immediately runs a validation check.

**Validation (_validate)**: This is a defensive programming step. It checks if the input data contains all the necessary columns (like GAME_ID and FGM). If any are missing, it raises a ValueError to prevent the program from running with broken data.

**Encapsulation (@property)**: The @property decorator allows you to access the data via box.data as if it were an attribute, but keeps the underlying \_data protected.

**Custom Representation (__repr__)**: This magic method defines what happens when you print() the object. Instead of just showing the table, it calculates and displays a summary header showing the total number of rows and unique games.

**2. Main Program Execution**

**Data Creation**: A standard pandas DataFrame is created containing raw basketball stats.

**Object Instantiation**: box = Boxscore(data=df) transforms the raw DataFrame into a Boxscore object.

**Display**: When print(box) is called, Python executes the \__repr_\_ method, printing the custom summary followed by the formatted data table.

**Key Benefits of this Approach**

**Data Integrity**: By using the validator, you guarantee that any code interacting with a Boxscore object can safely assume those specific columns exist.

**Readability**: The output is more informative than a standard DataFrame printout because it explicitly states the context (number of games represented).

**Maintenance**: If you later need to add a method to calculate "Total Points," you can add it directly to the class (e.g., box.calculate_points()), keeping your code organized and DRY (Don't Repeat Yourself).
