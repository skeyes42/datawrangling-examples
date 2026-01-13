## RPY2_example.py

This program demonstrates

**interoperability** by running R code directly inside a Python environment using the rpy2 library. It is the functional opposite of the reticulate library (which runs Python inside R).

Here is the breakdown of how it works in 2026:

1\. Data Initialization (Python)

The program starts in **Python**, creating a standard pandas.DataFrame containing basketball statistics. It performs an initial calculation for total points (PTS_PY) using vectorized pandas operations.

2\. The Conversion Bridge (pandas2ri)

One of the biggest challenges in cross-language programming is that R and Python store data differently in memory.

**pandas2ri**: This module is a "translator."

**localconverter**: This creates a temporary "bridge." Inside the with block, Python's pandas DataFrames are automatically translated into R's data.frame format so the R engine can understand them.

3\. Loading the R Environment

**r.source('RPY2_example.R')**: This command tells the embedded R engine to read and execute an external R script.

**r['calculate_points']**: This retrieves a reference to an R function named calculate_points that was defined inside that .R script. In Python, this becomes a callable object.

4\. Executing R Logic from Python

The line result = calculate_points_r(df) is the core of the program:

**Python** passes the df into the converter.

**rpy2** converts it to an R object.

The **R engine** runs its logic and returns a result.

The result is converted back into a **Python/Pandas** object for the final print statement.

5\. Accessing R Global Variables

The line print(r.message_from_r) shows that Python can "reach into" the R session's global environment. If the R script created a variable named message_from_r, Python can access it directly via the r object.

Summary of Workflow

| **Step**        | **Language** | **Component**                                                                                                           |
|-----------------|--------------|-------------------------------------------------------------------------------------------------------------------------|
| **Origin**      | Python       | Create and calculate data using pandas.                                                                                 |
| **Translation** | rpy2         | Convert pandas.DataFrame <br>![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ \rightarrow $$<br>→<br>R data.frame. |
| **Execution**   | R            | Run specific logic inside an embedded R session.                                                                        |
| **Retrieval**   | Python       | Receive the R result back as a Python object.                                                                           |

Why use this?

This approach is primarily used by Python developers who need to access **specialized R packages** (like LME4 for mixed-effects models or Forecast for time-series) that do not have equivalent or mature counterparts in the Python ecosystem.
