## RPY2_example.R

This R script is designed to be executed from a **Python** environment using the rpy2 library. It defines the logic that R will perform on data passed to it from Python.

**1. The calculate_points Function**

This is the core function that Python will call. In 2026 workflows, this is a standard way to leverage R's statistical syntax within a Python pipeline.

**Input (py_df)**: Although named py_df, by the time the data reaches this function, rpy2 has already converted the Python Pandas DataFrame into an **R data.frame**.

**Vectorized Calculation**: The line df\$PTS_R \<- df\$FGM \* 2 + df\$FG3M \* 3 + df\$FTM uses R's native vectorization. It calculates the points for every row simultaneously.

**Console Feedback**: The print statement provides a preview of the specific columns (PLAYER_ID, FGM, FG3M, FTM, and the new PTS_R) back to the terminal so the user can verify the R-side processing.

**Return Value**: The function returns the entire modified data frame. rpy2 will then catch this and convert it back into a Pandas DataFrame for the Python script to use.

**2. Global Variable (message_from_r)**

The line message_from_r \<- "Data processed in R" creates a character string in R’s global environment.

**Cross-Language Access**: Because this variable is defined globally in the R script, the Python side can access it at any time using the syntax rpy2.robjects.r.message_from_r. This is useful for passing status messages or metadata between the two languages.

**3. Key Interoperability Concepts**

**Data Type Mapping**

The script relies on rpy2's translation layer to ensure types remain consistent.

| **Feature**         | **Python Side (Pandas)** | **R Side (this script)** |
|---------------------|--------------------------|--------------------------|
| **Table Structure** | DataFrame                | data.frame               |
| **Missing Values**  | NaN or None              | NA                       |
| **Columns**         | Series                   | Vectors                  |

**Why use R logic here?**

Developers often use this pattern when:

**Validation**: They want to use R's unique formula syntax or specialized packages.

**Legacy Code**: They have existing, validated R functions that they want to incorporate into a newer Python-based production environment.

**Statistical Accuracy**: They prefer R’s handling of certain statistical edge cases (like specific rounding rules or factor levels).
