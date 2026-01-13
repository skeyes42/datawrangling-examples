## PlotBoxChart.py

This Python program extracts sports data from a database, calculates a custom performance metric, and generates a boxplot to compare performance between wins and losses. It is essentially a Python version of an R/ggplot2 workflow using the **plotnine** library.

Here is the breakdown of its components:

**1. Database Extraction**

The function get_boxscores handles the data retrieval:

It connects to a SQLite database (Boxscores.db) using the sqlite3 library.

It uses pd.read_sql_query to pull the entire "Boxscores" table into a pandas DataFrame.

The database path is constructed using an environment variable (EXAMPLES), making the script portable across different systems.

**2. Feature Engineering**

After loading the data, the script creates a new metric called **SCORING_EFFORT**:

It sums three columns row-by-row: FGM (Field Goals Made), FG3M (Three-Pointers Made), and FTM (Free Throws Made).

In R terms, this is the equivalent of a mutate() or pmap_dbl() operation.

**3. Visualization with Plotnine**

The script uses plotnine, which implements the "Grammar of Graphics" in Python (mimicking R's ggplot2 syntax):

**Aesthetics:** It maps the game outcome (WIN_LOSS) to the X-axis and the new SCORING_EFFORT metric to the Y-axis.

**Geometry:** It creates a **boxplot** (geom_boxplot) to show the distribution (median, quartiles, and outliers) of scoring effort.

**Styling:**

It uses scale_fill_grey() for a grayscale color palette.

It renames the X-axis labels from binary digits (0, 1) to human-readable text (Loss, Win).

It applies a minimal theme for a clean look.

**4. Output**

**Save:** The resulting chart is saved as a high-resolution PNG file (scoring_effort_boxplot.png) at 300 DPI.

**Console:** It prints "Done" to signal successful completion.
