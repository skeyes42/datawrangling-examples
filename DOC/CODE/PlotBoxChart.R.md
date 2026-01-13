## PlotBoxChart.R

This R program is the functional equivalent of the Python script you previously shared. It retrieves sports data from a database, calculates a combined scoring metric, and generates a boxplot to compare performance between wins and losses.

Here is the step-by-step explanation:

**1. Database Extraction Function**

The program defines a custom function getBoxscores to handle data retrieval:

**Connection:** It opens a connection to a SQLite database.

**Querying:** It uses dplyr syntax (tbl \|\> select(everything)) to reference the "Boxscores" table.

**Collection:** The collect() function executes the query and pulls the data from the database into R's memory as a data frame.

**Cleanup:** It ensures the connection is closed using dbDisconnect before returning the data.

**2. Feature Engineering**

Once the data is loaded into df, it creates a new metric called **SCORING_EFFORT**:

It uses mutate() and pmap_dbl() from the tidyverse to perform a row-wise sum.

For every row, it adds together **FGM** (Field Goals Made), **FG3M** (Three-Pointers Made), and **FTM** (Free Throws Made).

**3. Visualization with ggplot2**

The script uses ggplot2 to create a boxplot that visualizes the distribution of the scoring effort:

**Aesthetics:** The X-axis is the game outcome (WIN_LOSS), and the Y-axis is the calculated SCORING_EFFORT.

**Geometry:** geom_boxplot displays the median, quartiles, and potential outliers of the scoring data.

**Formatting:**

**scale_fill_grey()**: Sets the box colors to shades of gray.

**scale_x_discrete()**: Changes the labels on the X-axis from "0" and "1" to "Loss" and "Win."

**labs()**: Adds the title and axis titles.

**theme_minimal()**: Removes heavy background gridlines for a cleaner appearance.

**4. Comparison to the Python Version**

If you are comparing this to the previous Python code:

pmap_dbl(list(FGM, FG3M, FTM), sum) in R performs the same task as df[['FGM', 'FG3M', 'FTM']].sum(axis=1) in Python.

ggplot() in R is the direct inspiration for the plotnine library used in the Python script.

**Note:** The script loads the rhandsontable library at the top, but it is not actually used in the code provided (that library is typically used for creating interactive, Excel-like tables in Shiny apps).
