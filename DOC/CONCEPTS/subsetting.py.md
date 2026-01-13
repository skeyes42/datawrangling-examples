## subsetting.py

This Python program demonstrates various ways to select data from a **pandas DataFrame** and how the resulting **data type** (type) changes depending on the slicing syntax used.

Here is the breakdown of each experiment as of 2026:

**--- 1 --- Selecting a single column as a DataFrame**

**Syntax:** df[['GAME_ID']] (Double square brackets)

**Result:** **\<class 'pandas.core.frame.DataFrame'\>**.

**Explanation:** Using double brackets preserves the 2-dimensional table structure, returning a DataFrame with a single column.

**--- 2 --- Selecting a specific scalar value**

**Syntax:** df.iloc[0, 0]

**Result:** **\<class 'numpy.int64'\>** (or a similar NumPy integer type).

**Explanation:** The .iloc[row, column] accessor selects a single cell's exact value (a scalar). In pandas, numeric values are usually backed by the NumPy library for performance.

**--- 3 --- Selecting a single row**

**Syntax:** df.iloc[[0]] (Double brackets for the row index)

**Result:** **\<class 'pandas.core.frame.DataFrame'\>**.

**Explanation:** This selects the first row but maintains the DataFrame structure (it's a 1-row by 6-column table).

**--- 4 --- Selecting a single column as a Series**

**Syntax:** df.iloc[:, 0]

**Result:** **\<class 'pandas.core.series.Series'\>**.

**Explanation:** The .iloc accessor is location-based ([rows, columns]). This selects all rows (:) of the first column (0). A single column in pandas is natively a **Series** (a 1-dimensional structure).

**--- 5 --- Extracting column values (standard access)**

**Syntax:** df['GAME_ID'] (Single square brackets)

**Result:** **\<class 'pandas.core.series.Series'\>**.

**Explanation:** This is the most common and idiomatic way to access a column in pandas. It returns a 1-dimensional Series, effectively "dropping" the DataFrame wrapper, similar to how R's df[,1] works.

**Summary Table of Selectors**

| **Syntax**    | **Purpose**                           | **Resulting Type** |
|---------------|---------------------------------------|--------------------|
| df[['col']]   | Select one column, keep as a table    | DataFrame          |
| df.iloc[0, 0] | Select one single value by position   | numpy.int64        |
| df.iloc[[0]]  | Select one row as a table             | DataFrame          |
| df.iloc[:, 0] | Select one column by position         | Series             |
| df['col']     | Select one column by label (standard) | Series             |
