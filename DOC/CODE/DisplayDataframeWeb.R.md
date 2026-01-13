## DisplayDataframeWeb.R

This program is a **web application** built with R Shiny, a framework used to create interactive data dashboards. It allows users to view, search, and filter the "Boxscores" database through a professional web interface.

**1. Data Preparation (The "Back-end")**

Before the app launches, it performs a one-time data pull:

**Database Connection**: It uses [DBI](https://dbi.r-dbi.org/) and RSQLite to connect to the Boxscores.db file.

**Data Extraction**: Using dplyr, it selects all columns (everything()) and uses collect() to pull the data from the database into R's memory.

**Safety**: It immediately closes the database connection (dbDisconnect) so the file isn't locked while the app is running.

**2. The User Interface (UI)**

The ui object defines how the app looks:

**sidebarLayout**: Creates a classic dashboard look with a control panel on the left and a large data area on the right.

**Data Information**: The sidebar displays the total number of rows and columns found in the dataset.

**DTOutput**: This is a placeholder for a "DataTable," a high-performance interactive table.

**3. The Server Logic (The "Brain")**

The server function handles the interactivity:

**renderText**: Dynamically generates the row/column count text.

**renderDT**: This is the core of the app. It uses the DT (DataTables) package to create a table with several built-in features:

**filter = "top"**: Adds individual search boxes to the top of every column, allowing you to filter for specific teams, players, or stats simultaneously.

**searching = TRUE**: Enables a global search box in the top-right corner.

**pageLength = 10**: Shows 10 rows at a time so the page stays clean.

**ordering = TRUE**: Allows users to click on any column header to sort the data (e.g., clicking "Points" to see the highest-scoring games first).

**4. Execution**

The final line, shinyApp(ui, server), launches the application. In 2026, this remains the standard way to share data insights with non-technical users, as they can explore the database without needing to know SQL or R code.

**Summary**

This program converts a static database file into a **dynamic, searchable web tool**. It is particularly useful for sports analysts who need to quickly find specific game stats using a clean, user-friendly interface.
