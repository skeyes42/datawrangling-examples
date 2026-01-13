## PlotLineChart.R

This R program performs the same analysis as the Python script you previously reviewed: it connects to a basketball database, extracts data on team wins versus shooting percentages from the 2025 season, and generates a line plot to visualize the relationship between these two variables.

Here is a breakdown of the code using R-specific syntax and libraries:

**1. Data Retrieval**

**Environment Setup:** The script uses Sys.getenv("EXAMPLES") to dynamically locate the Boxscores.db database file on your system.

**Database Connection:** It uses the DBI and RSQLite libraries to open a connection to the SQLite database.

**Querying:** The R function dbGetQuery(con, ...) executes the exact same SQL command as the Python script: "SELECT FG3_PCT_AVG, SEASON_WINS FROM Season2025". This pulls the average 3-point percentage and total season wins data.

**Cleanup:** The connection is immediately closed with dbDisconnect(con).

**2. Visualization with ggplot2**

The program uses the ggplot2 library, which is the R standard for data visualization:

**Base Plot:** ggplot(season_data, aes(x = SEASON_WINS, y = FG3_PCT_AVG)) initializes the plot, mapping wins to the X-axis and 3FG% to the Y-axis.

**Geometric Layers:**

geom_line() draws the lines connecting the data points.

geom_point() draws the individual markers on the line.

Both layers use the same specific shade of blue (\#1f77b4) used in the Python Matplotlib example.

**Labels and Theme:**

labs() sets the main title, subtitle ("2025 Season"), and axis titles.

theme_minimal() provides a clean background.

The second theme() block is used for fine-tuning the look, making the titles bold and consistent with the Python version's style.

**Summary of the Goal**

The purpose of this R script is identical to the Python script: to visually explore the correlation in the 2025 season between how well a basketball team shoots from three-point range and how many games they ultimately win. The resulting graph helps to quickly identify if higher shooting accuracy consistently leads to more victories.
