## summarize.py

This Python program demonstrates how to perform data aggregation and grouping in **pandas** using **Named Aggregation**. This feature allows you to create summary statistics while simultaneously giving the new columns specific, descriptive names.

Here is a breakdown of each part of the code:

**1. Data Initialization**

The program creates a DataFrame representing a basketball box score with columns for Game ID, Team ID, Player ID, and various scoring metrics like field goals made (FGM), three-pointers (FG3M), and free throws (FTM).

**2. Overall Summary Statistics**

The df.agg() method is used on the entire DataFrame to perform global calculations.

-   **Mechanism:** It uses keyword arguments (like avg_fgm=...) to define the name of the output column.
-   **Result:** It returns a single row containing the average and total field goals made across all games and players.

**3. Summary by Team (Grouping)**

This section uses groupby('TEAM_ID') to split the data into groups based on the team identifier.

-   **Aggregation:** It applies different functions (mean and sum) to the FGM column for each team.
-   **.reset_index():** By default, groupby turns the grouping column (TEAM_ID) into the index. Using reset_index() moves TEAM_ID back into a regular column, making the result look like a standard flat table.

**4. Summary by Player (Counting Records)**

This final example demonstrates how to count rows within groups.

-   **size vs count:** It uses size to calculate games_played. In pandas, size counts the total number of rows in a group (including nulls), whereas count only counts non-null values.
-   **Result:** It shows the total field goals and the number of game appearances for each player.

**Summary of Key Methods**

| **Method**            | **Purpose**                                                         |
|-----------------------|---------------------------------------------------------------------|
| **agg()**             | Applies one or more aggregation functions to columns.               |
| **groupby()**         | Splits data into groups based on specific criteria.                 |
| **reset_index()**     | Converts the index back into a regular column for a cleaner output. |
| **Named Aggregation** | The syntax new_col=(column, function) to name results in one step.  |
