## PlotBarChart.R

This R program connects to a sports database to extract, process, and visualize the performance statistics of a specific player named "John."

Here is a breakdown of what each section does:

**1. Database Connection**

The script uses DBI and RSQLite to connect to a local database file named **Boxscores.db**. It retrieves the file path from an environment variable named "EXAMPLES."

**2. Data Retrieval and Joining**

It builds a SQL query using dplyr syntax to combine three separate database tables:

**Boxscores:** The primary table containing game statistics.

**Players:** Joined to match PLAYER_ID with the actual player name.

**Teams:** Joined to match TEAM_ID with the team name.  
The query filters for a player named **"John"** and removes the raw ID columns to clean up the data. The collect() function then pulls this data from the database into your local R environment as a dataframe.

**3. Data Reshaping**

The script transforms the data from a **"wide"** format to a **"long"** format using pivot_longer.

It collapses three specific columns—**FGM** (Field Goals Made), **FG3M** (Three-Pointers Made), and **FTM** (Free Throws Made)—into two columns: Stat_Type and Count.

This transformation is required for ggplot2 to plot multiple categories side-by-side.

The final reshaped data is saved to a file called **Results_Long.csv**.

**4. Visualization**

It creates a grouped bar chart using ggplot2 and ggpattern:

**X-axis:** Displays individual Game IDs.

**Y-axis:** Displays the count for each statistic.

**Patterns:** Instead of using colors, it uses different patterns (stripes, crosshatches, and circles) to distinguish between FGM, FG3M, and FTM. This is particularly useful for black-and-white printing or accessibility.

**5. Cleanup**

Finally, the script prints the chart to your screen, closes the database connection with dbDisconnect(con), and prints "Done" to the console.
