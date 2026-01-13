## class_example4.py

This Python program demonstrates **Object-Oriented Programming (OOP)** principles using Python Dataclasses, providing a more modern and concise way to handle data than traditional classes.

**1. The Class Hierarchy**

The program structure uses a parent-child relationship to manage basketball statistics:

**StatLine (Parent Class):** A @dataclass that defines the core shooting metrics.

**Properties (@property):** These allow methods like points or fg_pct to be accessed like attributes (e.g., game.points) rather than function calls (e.g., game.points()).

**Safety:** The percentage methods check for division by zero and return None (Optional) if no shots were taken.

**PlayerGame (Child Class):** Inherits all stats from StatLine and adds specific identifiers for the Game, Team, and Player. Because it inherits from StatLine, it automatically has access to the point and percentage calculations.

**2. Polymorphism and Method Overriding**

The method poly_print exists in both classes:

**Overriding:** The child class redefines the method.

**Execution:** When called, Python looks at the object's type. stat1.poly_print() triggers the parent logic, while pg1.poly_print() triggers the child logic. This is a core pillar of OOP.

**3. Data Integration (The "Constructor")**

The function player_games_from_df converts a pandas DataFrame into a list of Python objects:

**astype(int)**: Ensures the data types match the class definitions.

**Dictionary Unpacking (\*\*row)**: Converts each row of the DataFrame into a dictionary and "unpacks" it as arguments for the PlayerGame constructor. This is the Python equivalent of R's pmap.

**4. Inheritance Demo**

The final section proves that the child class successfully inherited the parent's logic:

**Usage:** It picks the first player performance from the list.

**Logic:** Even though points and fg_pct are not explicitly written inside the PlayerGame class, they work perfectly because they were inherited from StatLine.

**Verification:** It uses \__mro_\_ (Method Resolution Order) to show that PlayerGame is a subclass of StatLine.

**Comparison of Key Features**

| **Feature**           | **Python Implementation**    | **Benefit**                                      |
|-----------------------|------------------------------|--------------------------------------------------|
| **Data Container**    | @dataclass                   | Automatically writes \__init_\_ and \__repr__.   |
| **Inheritance**       | class PlayerGame(StatLine):  | Reuse math/logic across different entity types.  |
| **Calculated Fields** | @property                    | Clean syntax for derived data (like shooting %). |
| **Bulk Creation**     | List Comprehension + \*\*row | Efficiently turns table data into rich objects.  |
