## BoxscoresPandastable.py

This program integrates **Python and R** to fetch data and display it in a desktop application. It uses R to retrieve specialized "Boxscores" data and the Python library pandastable to show that data in a spreadsheet-like GUI.

**Key Components**

**R Integration (rpy2)**:  
The program uses rpy2 to run R code directly within Python.

It checks for and installs the R package **'S7'** if it is missing.

It loads an external R script (BoxscoresClass.R) from a path defined in the EXAMPLES environment variable.

The localconverter ensures that the data returned from the R function get_Boxscores_data is correctly transformed into a **Pandas DataFrame**.

**Data Handling (pandas)**:  
The retrieved data is stored as a Pandas DataFrame, the standard Python structure for tabular data.

**GUI Interface (tkinter & pandastable)**:

**Tkinter**: Provides the underlying windowing system for the desktop app.

**pandastable**: A specialized widget that allows users to interact with DataFrames like a spreadsheet.

**DataFrameViewer Class**: A custom class that initializes the table widget within a Tkinter frame, enabling features like a toolbar and status bar.

**Execution Workflow**

**Environment Setup**: Imports libraries and ensures the necessary R environment (S7 package) is ready.

**Data Extraction**: Reads an R file, executes it to fetch "Boxscores" data, and converts that output into a Python-friendly Pandas format.

**Visualization**: Launches a 600x400 pixel window displaying the data in an interactive table where users can view and potentially manipulate the results.
