## create_new_variable.py

1\. Data Initialization

The program creates a DataFrame representing basketball "box scores." It contains identifiers for games, teams, and players, along with three statistical columns: Field Goals Made (FGM), Three-Pointers Made (FG3M), and Free Throws Made (FTM).

2\. Mutate (Adding Columns)

The assign() method is used to mimic R's mutate.

What it does: It creates a new column called SCORING_EFFORT by adding three existing columns together.

Result: The new DataFrame contains all original columns plus the new one.

3\. Transmute (New Columns Only)

This section mimics R's transmute, which creates new variables and drops existing ones.

How it works: It starts with an empty selection boxscores_df[[]] and then uses assign().

Result: The resulting DataFrame only contains the SCORING_EFFORT column.

4\. Mutate Across (Bulk Transformation)

This replicates the across() function in R, which applies the same operation to multiple columns at once.

How it works:

It defines a list of columns to modify (cols_to_double).

It uses a dictionary comprehension with unpacking (\*\*) to dynamically create new column names (e.g., FGM_doubled) and assign them the value of the original column multiplied by two.

Result: The DataFrame keeps all original data and adds three new columns with doubled values.

Summary of Key Functions

| Concept       | Pandas Approach      | Description                                                                              |
|---------------|----------------------|------------------------------------------------------------------------------------------|
| Mutate        | .assign(new_col=...) | Adds new columns while preserving the original ones.                                     |
| Transmute     | df[[]].assign(...)   | Returns a DataFrame containing only the newly created columns.                           |
| Mutate Across | .assign(\*\*{...})   | Uses dictionary unpacking to apply a transformation to a list of columns simultaneously. |
