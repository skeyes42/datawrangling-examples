## anonymous1.py

This Python program demonstrates how to create a new column in a

pandas DataFrame by applying custom logic to each row using an **anonymous function** (lambda).

Here is the step-by-step explanation for 2026:

1\. Data Initialization

The program creates a DataFrame with three columns: id, value1, and value2. In pandas, this is the standard way to represent tabular data.

2\. The Lambda Function

The expression lambda row: row['value1'] \* 2 + row['value2'] defines a temporary, one-line function:

**Input**: It accepts an object representing a single **row** of data.

**Logic**: It retrieves the values from value1 and value2 for that row and calculates:

![](media/325472601571f31e1bf00674c368d335.gif)

$$
( v a l u e 1 \times 2 ) + v a l u e 2
$$

(𝑣𝑎𝑙𝑢𝑒1×2)+𝑣𝑎𝑙𝑢𝑒2

.

3\. The apply() Method with axis=1

The .apply() method is the mechanism used to execute the lambda function.

**axis=1**: This is the most important parameter. It tells pandas to process the data **row-by-row** (horizontally). If you omitted this, pandas would attempt to process column-by-column, which would fail in this context.

**Result**: The output of this operation is a new Series, which is assigned to a brand-new column named new_value.

4\. Summary of Calculations

The program performs the following operations:

| **id**  | **value1** | **value2** | **Calculation**                                                                           | **new_value** |
|---------|------------|------------|-------------------------------------------------------------------------------------------|---------------|
| 1       | 10         | 2          | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 1 0 \times 2 ) + 2 $$<br>(10×2)+2 | **22**        |
| 2       | 20         | 5          | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 2 0 \times 2 ) + 5 $$<br>(20×2)+5 | **45**        |
| 3       | 30         | 3          | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 3 0 \times 2 ) + 3 $$<br>(30×2)+3 | **63**        |

Comparison to 2026 Best Practices

While the apply() method is highly flexible for complex logic (like if/else statements), it is slower than **vectorized operations**. For simple math like this, the modern pandas performance guide recommends a direct approach:

python

\# Much faster than apply() for large datasets

df['new_value'] = df['value1'] \* 2 + df['value2']

Use code with caution.

Use the apply + lambda approach shown in your code specifically when you need to perform complex row-level logic that cannot be expressed as a simple mathematical formula.
