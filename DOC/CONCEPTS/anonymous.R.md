## anonymous.R

This R program demonstrates how to use an

**anonymous function** (also known as a **lambda**) inside a dplyr pipeline to perform custom row-wise calculations.

Here is the breakdown of the code:

1\. Data Creation

The program initializes a simple data frame with three columns: id, value1, and value2.

2\. The Anonymous Function

In R 2026, while the shorthand \\(x, y) syntax is common, this program uses the traditional function(x, y) { ... } syntax.

**What makes it "anonymous":** The function is defined and executed immediately without being assigned a name (like my_function).

**Logic:** It accepts two inputs (x and y) and returns the result of

![](media/325472601571f31e1bf00674c368d335.gif)

$$
( x \times 2 ) + y
$$

.

3\. Mutate Integration

The pipe operator (\|\>) passes the data frame into the mutate() function:

**new_value = (...)**: This defines the name of the new column.

**Execution**: The anonymous function is immediately followed by (value1, value2). This passes the vectors value1 and value2 as arguments x and y into the function.

4\. Vectorization

Because R is a vectorized language, the anonymous function does not run row-by-row in a slow loop. Instead, it processes the entire value1 and value2 columns simultaneously at the C-level, making it very efficient for large datasets.

Summary of Results

| **id**  | **value1** | **value2** | **Calculation**                                                                           | **new_value** |
|---------|------------|------------|-------------------------------------------------------------------------------------------|---------------|
| 1       | 10         | 2          | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 1 0 \times 2 ) + 2 $$<br>(10×2)+2 | **22**        |
| 2       | 20         | 5          | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 2 0 \times 2 ) + 5 $$<br>(20×2)+5 | **45**        |
| 3       | 30         | 3          | ![](media/325472601571f31e1bf00674c368d335.gif)<br>$$ ( 3 0 \times 2 ) + 3 $$<br>(30×2)+3 | **63**        |

Why use this?

While you could achieve the same result with mutate(new_value = value1 \* 2 + value2), using an anonymous function is useful when you have **complex logic** that you want to keep contained within the pipeline without cluttering your global environment with single-use functions.
