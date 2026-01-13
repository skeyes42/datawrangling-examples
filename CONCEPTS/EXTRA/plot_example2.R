library(ggplot2)
library(dplyr)
library(tidyr)

sink("plot_example2.txt")  

my_data <- tibble::tribble(
  ~GAME_ID, ~TEAM_ID, ~PLAYER_ID, ~FGM, ~FG3M, ~FTM,
      1000,      100,          1,   10,    12,   12,
      1000,      100,          2,    4,     4,    7,
      1000,      200,          3,    2,     6,    5,
      1000,      200,          4,    8,     2,    7,
      2000,      100,          1,   10,     4,   10,
      2000,      100,          2,   11,     5,    4,
      2000,      300,          5,    8,    10,    9,
      2000,      300,          6,    7,     6,    3
)

# Reshape the data using pivot_longer
my_data_long <- my_data |>
  pivot_longer(
    cols = c(FGM, FG3M, FTM),
    names_to = "stat_type",
    values_to = "value"
  )

# View the reshaped data structure
print(my_data_long, n = Inf)

# Create a grouped bar chart showing all three statistics
ggplot(my_data_long, aes(x = factor(PLAYER_ID), y = value, fill = stat_type)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(
    title = "Player Statistics by Type",
    x = "Player ID",
    y = "Count",
    fill = "Statistic"
  ) +
  theme_minimal()

ggsave("my_plot_grouped.png", width = 10, height = 6)

sink()