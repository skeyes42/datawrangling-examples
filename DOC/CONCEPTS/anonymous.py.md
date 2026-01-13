## anonymous.py

This Python program demonstrates how to use an

**anonymous function** (known as a **lambda**) to create a new column in a pandas DataFrame based on multiple existing columns.

Here is the step-by-step explanation:

1\. Data Initialization

The program creates a DataFrame with three rows and three columns: id, value1, and value2.

2\. The Lambda Function

The expression lambda row: row['value1'] \* 2 + row['value2'] is a small, one-line function without a name.

**Input**: It takes a single object (which we named row).

**Logic**: It accesses the values in the 'value1' and 'value2' columns for that specific row and calculates

![](media/325472601571f31e1bf00674c368d335.gif)

$$
( v a l u e 1 \times 2 ) + v a l u e 2
$$

(𝑣𝑎𝑙𝑢𝑒1×2)+𝑣𝑎𝑙𝑢𝑒2

.

3\. The apply() Method

The apply() function is used to run the lambda across the DataFrame.

**axis=1**: This is the most critical parameter. It tells pandas to apply the function **row-wise**. If this were axis=0, the function would try to operate on entire columns, which would cause an error in this specific context.

**Assignment**: The results of these row-by-row calculations are stored in a brand-new column named new_value.

4\. Summary of Calculations

The program performs the following math for each row:

| **id**  | **value1** | **value2** | **Calculation**                                                                           | **new_value** |
|---------|------------|------------|-------------------------------------------------------------------------------------------|---------------|
| 1       | 10         | 2          | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 1 0 \times 2 ) + 2 $$<br>(10×2)+2 | **22**        |
| 2       | 20         | 5          | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 2 0 \times 2 ) + 5 $$<br>(20×2)+5 | **45**        |
| 3       | 30         | 3          | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 3 0 \times 2 ) + 3 $$<br>(30×2)+3 | **63**        |

Performance Note for 2026

While apply(axis=1) is very readable and flexible for complex logic, it is generally slower than **vectorized operations**. For this specific math, a more efficient "pandas-native" way would be:  
df['new_value'] = df['value1'] \* 2 + df['value2']

You should use the lambda approach shown in your program primarily when your logic involves complex if-else statements or external library calls that cannot be easily vectorized.
