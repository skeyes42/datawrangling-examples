## chaining2.py

Key Components

1\. Data Definition  
The program creates a DataFrame from a list of dictionaries. It represents basketball box score stats (Game ID, Team ID, Player ID, and shot types).

2\. The peek Function

def peek(data, message="Data:"):

print(data.to_markdown(index = False))

return data

Use code with caution.

This is a custom helper function designed for use within a pandas pipe.

It prints the current state of the DataFrame in a clean, Markdown-formatted table.

Crucially, it returns the data object unchanged, allowing the method chain to continue.

3\. The Method Chain  
The calculation is performed in two steps:

.assign(...): It calculates a new column, SCORING, using the formula:

![](media/325472601571f31e1bf00674c368d335.gif)

$$
( 2 \times \text{Field Goals} ) + ( 3 \times \text{3-Pointers} ) + \text{Free Throws}
$$

(2×Field Goals)+(3×3-Pointers)+Free Throws

.

.pipe(peek, ...): It "pipes" the transformed DataFrame into the peek function. This triggers the print statement so you can see the results of the calculation immediately without needing a separate print() call at the end.
