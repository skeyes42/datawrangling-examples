## Correlation.R

This R program is a statistical script designed to calculate a **correlation matrix** for basketball performance metrics. It identifies how strongly different statistics (like points, assists, and rebounds) are related to one another.

**1. Data Extraction & Cleanup**

The program starts by pulling data from a SQLite database using the [DBI](https://dbi.r-dbi.org/) and dplyr packages:

**Database Connection**: It targets the Boxscores.db file located in a path defined by the EXAMPLES environment variable.

**Column Filtering**: It uses select(-GAME_ID, -PLAYER_ID, -TEAM_ID) to remove identification numbers. These are "ID" fields that would interfere with mathematical calculations because their numerical values are arbitrary and not representative of performance.

**The "Collect" Step**: Because dplyr is "lazy" when working with databases, the collect() function is used to finally execute the query and pull the data from the database into R’s memory as a data frame.

**Resource Management**: It immediately uses dbDisconnect(con) to close the database connection, which is a best practice in 2026 to ensure data integrity and free up system resources.

**2. Statistical Calculation**

The core of the program is the cor() function:

**where(is.numeric)**: This ensures that only columns containing numbers are passed to the correlation function, automatically ignoring any text-based columns like player names.

**use = "complete.obs"**: This is a safety setting that handles missing data. If a player has a blank entry for a specific stat, this setting tells R to skip that row for that specific calculation rather than returning an error or NA.

**The Result**: It produces a table where every statistic is compared against every other statistic. The values range from **-1 to 1**:

**Near 1.0**: Strong positive relationship (e.g., as Field Goal Attempts go up, Points usually go up).

**Near 0.0**: No relationship (e.g., a player's jersey number likely has no correlation with their shooting percentage).

**Near -1.0**: Strong inverse relationship.

**3. Output Formatting**

**options(width = 200)**: This tells R to use more horizontal space in the console when printing. This is helpful for correlation matrices, which are often very wide, ensuring the table doesn't "wrap" and becomes difficult to read.

**Summary**

This program is an essential tool for 2026 sports analysts. It allows you to quickly see which aspects of the game are linked together—for instance, determining if high assist totals are statistically correlated with higher team shooting percentages.
