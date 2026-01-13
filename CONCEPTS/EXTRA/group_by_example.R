library(dplyr)

# Create some sample data
sales <- tibble(
  region = c("North", "North", "South", "South", "East", "East"),
  product = c("A", "B", "A", "B", "A", "B"),
  revenue = c(100, 150, 200, 175, 125, 225)
)

# Capture the grouped object
grouped_sales <- sales |> group_by(region)

# Inspect what we have
class(grouped_sales)
# [1] "grouped_df" "tbl_df" "tbl" "data.frame"

# See the grouping structure
group_vars(grouped_sales)    # Returns: "region"
group_keys(grouped_sales)    # Returns tibble of unique group values
n_groups(grouped_sales)      # Returns: 3

# The group metadata lives in an attribute
group_data(grouped_sales)
# Returns a tibble showing each group and row indices

# Now we can reuse this grouped object multiple times
# without re-executing group_by()
cat("\nSum of Revenue")
grouped_sales |> summarise(total = sum(revenue)) |>  print()
cat("\nMean of Revenue")
grouped_sales |> summarise(avg = mean(revenue))
cat("\nRevenue Percent")
grouped_sales |> mutate(pct_of_region = revenue / sum(revenue) * 100)

# We can also iterate over groups explicitly
print(
  group_split(grouped_sales)  # Returns a list of tibbles, one per group
)

# Or apply a function to each group
print(
  group_map(grouped_sales, ~ .x |> slice_max(revenue, n = 1))
)