## PlotBarChart.py

This Python program is a specialized data visualization script designed for **player performance analysis**. It extracts specific shooting statistics for a player named "John" and generates a patterned bar chart to compare different types of made shots across multiple games.

**1. Data Extraction (SQL Join)**

The program connects to Boxscores.db and performs a three-way SQL JOIN. It links raw game stats to the Players and Teams tables to replace ID numbers with actual names. It filters the results specifically for **"John"**, ensuring the analysis focuses on a single individual's performance.

**2. Data Reshaping (Melting)**

To prepare the data for visualization, the script uses pd.melt().

**The Problem**: In the database, FGM (Field Goals Made), FG3M (3-Pointers Made), and FTM (Free Throws Made) are in separate columns.

**The Solution**: "Melting" stacks these columns into a "Long Format." This creates a new column called Stat_Type and a Count column, which is the standard format required for complex grouped plotting.

**3. Visualization with Matplotlib**

The script creates a **Grouped Bar Chart** with unique visual accessibility features:

**Patterns (Hatches)**: Instead of relying solely on color, it uses different patterns (///, xxx, ...) to distinguish between the three shot types. This is a professional standard in 2026 for making charts accessible to colorblind users or readable in black-and-white prints.

**Custom Layout**: It calculates the exact position of each bar (xi + i\*width) so that the three stats for each game appear side-by-side above the corresponding Game ID.

**Export**: The chart is saved as a high-resolution PNG (bar_chart_patterns.png) for use in reports.

**4. Execution Flow**

**Locates Database**: Finds the file via the EXAMPLES environment variable.

**Queries & Cleans**: Pulls "John's" data and drops unneeded ID columns.

**Saves Intermediate Data**: Exports the reshaped long-format data to Results_Long.csv for audit purposes.

**Generates Plot**: Builds the bar chart, displays it, and saves the image.

**Closes Connection**: Safely disconnects from the database.

**Summary**

This program is an **Athlete Performance Dashboard**. It provides a clear, visual comparison of how a player scored their points—showing the balance between regular field goals, 3-pointers, and free throws across their recent game history.
