## class_example4.R

This program demonstrates advanced **Object-Oriented Programming (OOP)** in R using the S7 system. It focuses on **inheritance**, **polymorphism**, and functional data processing.

**1. The Class Hierarchy**

The program defines two classes to handle basketball data with a parent-child relationship:

**StatLine (Parent Class):** Defines the core statistical properties (Field Goals, 3-Pointers, Free Throws) as integers.

**PlayerGame (Child Class):** Inherits all properties from StatLine and adds metadata specific to a single performance: GAME_ID, TEAM_ID, and PLAYER_ID.

**2. Generics and Methods (Inheritance)**

The program uses new_generic() and method() to define behaviors that work across these classes:

**Calculated Stats:** It defines methods to calculate shooting percentages (fg_pct, fg3_pct, ft_pct) and total points (points).

**Inheritance in Action:** Because PlayerGame is a child of StatLine, the points() method written for StatLine automatically works on PlayerGame objects. You don't have to rewrite the math for the child class.

**3. Polymorphism**

The poly_print generic demonstrates **polymorphism** (the ability of different classes to respond to the same function call in their own way):

When called on a StatLine object, it prints "From parent class".

When called on a PlayerGame object, it prints "From child class".  
S7 automatically "dispatches" the call to the most specific method available for that object's class.

**4. Data Integration (The "Constructor")**

The function player_games_from_df bridges the gap between traditional data frames and S7 objects:

**dplyr**: It uses select() and mutate(across(...)) to ensure all columns are formatted as integers.

**purrr::pmap**: This is the "constructor." It iterates through every row of the data frame and passes the values into the PlayerGame class creator, resulting in a **List of Objects** (all_games).

**5. Summary of Results**

The **Demo** section proves the architecture works:

It prints the polymorphic messages to show method dispatch is working.

It extracts one object from the list and calculates its points and percentages using the inherited methods.

It verifies that game1 is indeed a PlayerGame object that inherits from the StatLine parent.

**Why use this?**

This approach is highly useful for **complex analytical pipelines** where you want to ensure that a "StatLine" always follows specific rules, regardless of whether it belongs to a Player, a Team, or an entire Season.
