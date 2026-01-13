## subsetting.R

This R program demonstrates the different ways to subset a **data.frame** and how R changes the resulting **data type (class)** based on the syntax used.

Here is the breakdown of each experiment as of 2026:

**--- 1 --- Subsetting a Column (List Style)**

**Syntax:** df[1]

**Result:** A **data.frame**.

**Explanation:** Using a single index inside single brackets treats the data frame like a **list** of columns. It returns a "mini" data frame containing only the first column.

**--- 2 --- Subsetting a Single Cell**

**Syntax:** df[1,1]

**Result:** **numeric**.

**Explanation:** By providing both a row index and a column index [row, col], R extracts the exact value at that coordinate. Since the data is numeric, the result is a simple numeric value.

**--- 3 --- Subsetting a Row**

**Syntax:** df[1,]

**Result:** **data.frame**.

**Explanation:** Leaving the column index blank tells R to take the entire first row. Because a row can contain multiple different data types (strings, numbers, etc.), R keeps it wrapped in a data frame.

**--- 4 --- Subsetting a Column (Matrix Style)**

**Syntax:** df[,1]

**Result:** **numeric** (a vector).

**Explanation:** By providing a comma but leaving the row index blank, you are asking for the entire first column. By default, R **drops** the data frame structure and simplifies it into a basic vector.

**--- 5 --- Extracting a Column (Double Brackets)**

**Syntax:** df[[1]]

**Result:** **numeric** (a vector).

**Explanation:** Double brackets [[ ]] are used to "reach inside" the data frame and pull out the raw data. This is the standard way to extract a column as a vector regardless of the data frame's dimensions.

**Summary Table**

| **Syntax** | **Resulting Class** | **Description**                         |
|------------|---------------------|-----------------------------------------|
| df[1]      | data.frame          | A table with 1 column.                  |
| df[1,1]    | numeric             | A single value.                         |
| df[1,]     | data.frame          | A table with 1 row.                     |
| df[,1]     | numeric             | A column converted to a vector.         |
| df[[1]]    | numeric             | Direct extraction of the column vector. |
