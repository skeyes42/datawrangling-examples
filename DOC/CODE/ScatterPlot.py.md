## ScatterPlot.py

This program performs a full data pipeline: it **joins multiple database tables**, cleans the resulting data, and generates a **high-quality scatter plot** visualizing basketball performance.

Here is a breakdown of its operations for 2026:

**1. Database Integration (SQL Joins)**

The program uses a sophisticated SQL query to combine data from three separate tables:

**Boxscores (b)**: The primary table containing numerical stats (points, shots, etc.).

**Players (p)** and **Teams (t)**: These are joined using LEFT JOIN on their respective IDs.

**Purpose**: This replaces cryptic IDs (like "P101") with actual names (like "LeBron James") and team names, making the final data human-readable.

**2. Data Cleaning with Pandas**

After loading the joined data into a DataFrame, the script performs two cleanup steps:

**Column Removal**: It drops the PLAYER_ID and TEAM_ID columns using results_df.drop. Since it already has the names from the join, these ID columns are now redundant and would clutter the analysis.

**Resource Management**: It calls con.close() early. Once the data is in the DataFrame, the database connection is no longer needed.

**3. Headless Visualization Setup**

**matplotlib.use('Agg')**: This is a critical configuration for 2026 environments like web servers, automated scripts, or cloud notebooks. It tells Python to render the plot "headless" (in memory) rather than trying to open a pop-up window on a monitor.

**4. Advanced Visualization (Seaborn)**

The program uses **Seaborn** to create a scatter plot with specific aesthetic choices:

**Metrics**: It plots **FG3M** (3-pointers made) on the X-axis against **FGM** (total field goals made) on the Y-axis.

**Style vs. Hue**: By using style='Player' and a fixed color='gray', the plot distinguishes players using different **marker shapes** (circles, squares, crosses) rather than colors. This is an excellent practice for accessibility (color-blind friendliness) or black-and-white printing.

**Legend Positioning**: bbox_to_anchor=(1.05, 1) moves the legend outside the main plot area so it doesn't overlap the data points.

**5. File Output**

Instead of showing the plot on screen, it saves a professional-grade file:

**scatter_plot.png**: Saved with **300 DPI** (high resolution suitable for print).

**bbox_inches='tight'**: Ensures that the legend and labels aren't cut off at the edges of the image.

**Summary of the Output**

You will get a high-resolution image showing the relationship between 3-point shooting and overall scoring. Players who appear toward the top-right are the most productive scorers from distance, with each player represented by a unique symbol.
