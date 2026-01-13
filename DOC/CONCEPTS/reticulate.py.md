## reticulate.py

This Python script is designed to be called from

**R** via the reticulate library. It acts as the "Python side" of a cross-language data processing workflow.

Here is an explanation of its components:

1\. The calculate_points Function

This function is intended to receive data directly from an R session.

**Data Conversion:** When R passes a data frame to this function, reticulate converts it into a format Python understands. The line df = pd.DataFrame(r_df) ensures it is treated as a pandas DataFrame.

**Logic:** It calculates a new column, PTS_PY, using the formula:

![](media/325472601571f31e1bf00674c368d335.gif)

$$
( F G M \times 2 ) + ( F G 3 M \times 3 ) + F T M
$$

.

**Return Value:** The function returns the modified DataFrame back to the R environment.

2\. Global Variable (df_python)

At the bottom of the script, a DataFrame named df_python is created.

**Accessibility:** In the 2026 data science ecosystem, this is a common way to "statefully" share data. Because this variable is defined in the global scope of the Python script, an R user can access it at any time using the syntax py\$df_python.

3\. Key Concepts demonstrated

**Automatic Type Mapping**

The script relies on reticulate's ability to map types between the two languages:

| **R Type**           | **Python Type**  |
|----------------------|------------------|
| data.frame or tibble | pandas.DataFrame |
| numeric              | float            |
| integer              | int              |

**Vectorized Operations**

The line df['PTS_PY'] = ... uses **pandas vectorization**. Instead of looping through rows one by one, Python calculates the points for every row in the table simultaneously at the C-level, which is significantly faster for large basketball datasets.

Summary of execution flow

**R** calls calculate_points(df).

**Python** receives the data, adds the PTS_PY column, and prints a preview to the console.

**Python** returns the updated table to R.

**R** can later "peek" into the Python environment to grab the df_python status message.
