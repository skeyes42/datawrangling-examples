## anonymous1.R

This R program demonstrates how to use the

**purrr** package (part of the Tidyverse) to perform row-wise calculations within a dplyr pipeline.

Specifically, it uses **functional programming** to handle multiple column inputs simultaneously.

1\. Data Initialization

The program creates a standard data frame with three columns: id, value1, and value2.

2\. The pmap_dbl Function

The core of this program is pmap_dbl(), which stands for **"parallel map"** returning a **double** (numeric) vector.

**The Input**: It takes a list(value1, value2). This aligns the elements of both columns row-by-row.

**The Anonymous Function**: The \~ .x \* 2 + .y syntax is a shorthand for an anonymous function.

.x refers to the first element in the list (value1).

.y refers to the second element in the list (value2).

**The Logic**: For every row, it calculates

![](media/325472601571f31e1bf00674c368d335.gif)

$$
( v a l u e 1 \times 2 ) + v a l u e 2
$$

(𝑣𝑎𝑙𝑢𝑒1×2)+𝑣𝑎𝑙𝑢𝑒2

.

3\. Mutate Integration

By wrapping pmap_dbl inside mutate(), the program creates a new column called new_value and populates it with the results of the mapping operation.

4\. Summary of Calculations

| **id**  | **value1 (.x)** | **value2 (.y)** | **Logic (.x \* 2 + .y)**                                                                  | **new_value** |
|---------|-----------------|-----------------|-------------------------------------------------------------------------------------------|---------------|
| 1       | 10              | 2               | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 1 0 \times 2 ) + 2 $$<br>(10×2)+2 | **22**        |
| 2       | 20              | 5               | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 2 0 \times 2 ) + 5 $$<br>(20×2)+5 | **45**        |
| 3       | 30              | 3               | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 3 0 \times 2 ) + 3 $$<br>(30×2)+3 | **63**        |

Why use purrr::pmap instead of standard mutate?

While a simple mutate(new_value = value1 \* 2 + value2) would work here, the purrr approach is superior when:

**Complexity**: Your function is complex and cannot be easily vectorized.

**Robustness**: You are working with list-columns or want to ensure strict type-checking (the \_dbl suffix ensures the output is always a number).

**Scalability**: You need to iterate over more than two columns (you can use ..1, ..2, ..3, etc., for larger lists).

Thank you

Your feedback helps Google improve. See our [Privacy Policy](https://policies.google.com/privacy?hl=en).

Share more feedbackReport a problemClose
