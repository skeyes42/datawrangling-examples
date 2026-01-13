library(dplyr) 
library(purrr)
# Create a sample data frame
df <- data.frame(
  id = 1:3, 
  value1 = c(10, 20, 30),
  value2 = c(2, 5, 3)
)

# Use an anonymous function with mutate to create a new column
# The anonymous function calculates (value1 * 2) + value2   

df_modified_purrr <- df %>%
  mutate(new_value = pmap_dbl(list(value1, value2), ~ .x * 2 + .y))

print(df_modified_purrr)

