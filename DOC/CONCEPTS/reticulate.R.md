## reticulate.R

This program demonstrates

**interoperability** between R and Python using the **reticulate** library. It allows you to share data and execution logic across both languages in a single workflow.

Here is a breakdown of the steps:

1\. Data Creation in R

The program starts by creating a basketball dataset using tibble::tribble(). It performs an initial calculation in R, creating a column PTS_R using standard R vector arithmetic.

2\. Passing Data to Python

The line source_python("reticulate.py") is the bridge. It executes a Python script (which must exist in the same directory). Any functions defined in that Python script, such as calculate_points(), become available to call directly in R as if they were R functions.

3\. Executing Python Logic

The R variable df (an R data frame) is passed into the Python function result \<- calculate_points(df).

**Automatic Conversion:** reticulate automatically converts the R **Data Frame** into a Python **Pandas DataFrame** behind the scenes [1].

**Result:** The Python function processes the data and returns a result back to R.

4\. Accessing the Python Environment (py\$)

The program demonstrates two-way communication:

**The py object:** When using reticulate, the py object acts as a gateway to the global Python environment.

**Variable Retrieval:** By calling py\$df_python, R reaches into the Python session and pulls back a variable named df_python.

**Conversion Back:** The Pandas DataFrame is converted back into an R data frame (specifically a tibble or data.frame) for use in R.

Summary of the Workflow

| **Step**     | **Language**                                                                          | **Action**                                                                  |
|--------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Setup**    | R                                                                                     | Create df and load reticulate.                                              |
| **Bridge**   | R <br>![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ \rightarrow $$<br>→<br>Py | source_python() makes Python code available to R.                           |
| **Process**  | Py                                                                                    | Python logic manipulates the data (e.g., in a function or global variable). |
| **Retrieve** | Py <br>![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ \rightarrow $$<br>→<br>R | Use py\$variable_name to bring results back into R.                         |

Why use this?

This is highly effective in 2026 for data science workflows where you want to use **R** for its superior statistical plotting (ggplot2) but need **Python** for specific machine learning libraries (scikit-learn, PyTorch) or pre-existing Python utility scripts [2].
