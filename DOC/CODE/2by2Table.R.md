## 2by2Table.R

This R program performs a "database-to-table" workflow by retrieving basketball statistics from a database and organizing them into a formatted frequency table.

As of 2026, it uses modern **Tidyverse**-style syntax to handle data cleaning and analysis.

**1. Data Retrieval**

**Database Connection:** It establishes a connection to a local SQLite file named Boxscores.db using the DBI and RSQLite libraries.

**Lazy Querying:** It uses dplyr and dbplyr to build a query for the Boxscores table without immediately pulling data into R. It selects two columns:

**FGM:** Field Goals Made.

**FG3M:** Three-Point Field Goals Made.

**Collection:** The collect() function finally executes the query and brings the results into R as a standard data frame.

**2. Categorization (Mutation)**

The program uses mutate() and ifelse() to convert numeric scores into categorical "factors":

**3-Pointers (FG3M):** Values \> 2 are labeled **"High 3P"**, others are **"Low 3P"**.

**Total Field Goals (FGM):** Values \> 5 are labeled **"High FG"**, others are **"Low FG"**.

It explicitly sets the levels of these factors to ensure the final table is ordered consistently (e.g., "Low" before "High").

**3. Contingency Table Generation**

The core of the program uses the tabyl() function from the janitor library:

**Frequency Counting:** It creates a 2x2 table showing the count of observations for every combination of the categories (e.g., how many "High 3P" players also had "High FG").

**Result:** Unlike the base R table() function, tabyl() returns a clean, Tidyverse-compatible data frame that is easier to read and format
