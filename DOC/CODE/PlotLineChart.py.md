## PlotLineChart.py

This Python program retrieves 2025 sports statistics from a database and creates a line plot to analyze the relationship between a team's shooting accuracy and their total wins.

Here is a breakdown of the steps:

**1. Data Retrieval**

**Environment Setup:** The script uses os.getenv to find the database location stored in the "EXAMPLES" system variable.

**Database Connection:** It connects to a SQLite database (Boxscores.db) and pulls data from a specific table named **Season2025**.

**Specific Metrics:** It selects two specific columns: FG3_PCT_AVG (Average 3-point field goal percentage) and SEASON_WINS.

**2. Data Preparation**

**Sorting:** The program uses pandas (sort_values) to organize the data by the number of wins. This is a critical step for line plots; without sorting, the line would zig-zag back and forth across the screen randomly.

**3. Visualization with Matplotlib**

Unlike the previous scripts that used "Grammar of Graphics" (ggplot2/plotnine), this script uses Matplotlib, a lower-level plotting library that offers precise control over every element:

**Plot Style:** It draws a blue line (\#1f77b4) connecting circular markers (marker='o').

**Aesthetics:**

It applies the seaborn-v0_8-whitegrid style for a clean, professional background.

It adds a **Subtitle** ("2025 Season") in gray to provide context.

It bolds the axis labels and title for better readability.

**Grid:** It enables a light grid (alpha=0.3) to help the viewer trace the values on the Y-axis.

**4. Summary of the Goal**

The program aims to visualize a **trend**: it shows whether teams with higher 3-point shooting percentages generally achieved more wins during the **2025 season**. By using a line plot with markers, it highlights the progression and specific data points for each win-total tier.

**Note on 2026 Context:** As we are currently in **2026**, this script serves as a retrospective analysis of the completed **2025 season** data.
