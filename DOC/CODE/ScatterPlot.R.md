## ScatterPlot.R

This R program performs an end-to-end data analysis workflow: it connects to a database, performs complex table joins using **dbplyr**, and creates a professional visualization using **ggplot2**.

Here is the explanation of the code for 2026:

**1. Database Integration (Relational Joins)**

The program uses left_join to combine three separate tables within the **Boxscores.db** database. Instead of writing raw SQL, it uses R syntax to:

Link the core **Boxscores** data with the **Players** and **Teams** tables.

**Rename on the fly:** It renames PLAYER_NAME to Player during the join to make the final data frame cleaner.

**Clean up:** It removes the ID columns (PLAYER_ID, TEAM_ID) using select(-...) because the actual names are now available.

**2. "Lazy" Query Execution**

A key feature of this script is its efficiency. The query object is a "lazy" reference. R does not actually pull the data from the database until the collect() command is called. This allows the database engine to handle the heavy lifting of joining and sorting before sending the final results to R.

**3. Advanced Visualization (ggplot2)**

The program creates a scatter plot to compare **FG3M** (3-pointers made) against **FGM** (total field goals made). Notable features include:

**Shape Mapping:** It maps each Player to a specific geometric shape (shape = factor(Player)).

**Manual Scales:** scale_shape_manual(values = c(21, 22, 23, 24, 25, 8)) specifically assigns shapes like circles, squares, and diamonds. Shapes 21–25 are particularly useful because they allow for separate "fill" and "border" colors.

**Aesthetics:** It uses theme_minimal() for a clean look and bolds the title for better readability.

**4. Logic & Purpose**

**Goal:** To visualize scoring efficiency and shooting profiles.

**Insights:** Players high on the Y-axis are high-volume scorers; players far to the right on the X-axis are 3-point specialists.

**Accessibility:** By using different shapes instead of just colors, the resulting chart remains readable in black-and-white or for users with color vision deficiencies.

**5. Prerequisites for 2026**

To run this successfully today in 2026, ensure:

The RSQLite and DBI packages are installed.

The EXAMPLES environment variable is set to the folder containing your database.

The database contains the tables Boxscores, Players, and Teams with the matching ID columns.
