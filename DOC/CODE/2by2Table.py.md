## 2by2Table.py

This Python program retrieves basketball statistics from a database and organizes them into a **contingency table** (cross-tabulation) to analyze the relationship between two specific metrics.

Here is a breakdown of what the code does step-by-step:

**1. Data Retrieval**

**Database Connection:** It locates a SQLite database file named Boxscores.db using an environment variable path.

**SQL Query:** It uses pandas.read_sql_query to extract two columns from the Boxscores table:

**FGM:** Field Goals Made (total shots made).

**FG3M:** Three-Point Field Goals Made.

**2. Data Categorization (Binning)**

The program converts these raw numbers into "High" or "Low" categories using pandas.cut:

**3-Pointers (FG3M):**

**Low 3P:** 0 to 2 shots made.

**High 3P:** More than 2 shots made.

**Total Field Goals (FGM):**

**Low FG:** 0 to 5 shots made.

**High FG:** More than 5 shots made.

**3. Categorical Ordering**

It explicitly sets the order of the FG3M_category to ensure that when the table is printed, "Low 3P" appears before "High 3P" for better readability.

**4. Cross-Tabulation**

Finally, it uses pandas.crosstab to create a 2x2 frequency table. The output will look something like this:

| **FG3M_category** | **Low FG** | **High FG** |
|-------------------|------------|-------------|
| **Low 3P**        | Count      | Count       |
| **High 3P**       | Count      | Count       |

**The Goal:** This program helps a researcher or analyst quickly see if players who make many three-pointers (High 3P) also tend to have a high volume of total field goals (High FG).
