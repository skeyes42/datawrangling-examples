library(dplyr)
# Create a sample data frame
df <- data.frame(
       id = 1:3,
       value1 = c(10, 20, 30),        
       value2 = c(2, 5, 3)
    )
# Use an anonymous function with mutate to create a new column
# The anonymous function calculates (value1 * 2) + value2
df_modified <- df |>
  mutate(new_value = (function(x, y) { x * 2 + y })(value1, value2))
     print(df_modified)
