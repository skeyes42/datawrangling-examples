# Load necessary libraries
# If you don't have them installed: install.packages("tidyverse")
library(tidyverse)

# Your initial data frame
df <- tibble::tribble(
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

# 1. Reshape the data from wide to long using pivot_longer()
# We move the shot types (FGM, FG3M, FTM) into a single 'shot_type' column, 
# and their corresponding values into a 'value' column.
df_long <- df %>%
  pivot_longer(
    cols = c(FGM, FG3M, FTM),  # Columns to pivot
    names_to = "shot_type",    # New column name for the variable types
    values_to = "value"        # New column name for the values
  )

# View the reshaped data
print('---- long format dataframe ----')
print(df_long)
cat('\n')

# 2. Create a ggplot visualization
ggplot(df_long, aes(x = factor(PLAYER_ID), y = value, fill = shot_type)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8)) +
  facet_wrap(~ GAME_ID, scales = "free_x") +
  labs(
    title = "Player Scoring Contributions by Shot Type Across Games",
    x = "Player ID",
    y = "Count",
    fill = "Shot Type"
  ) +
  theme_minimal() +
  scale_fill_brewer(palette = "Set2")
  ggsave("player_scoring_contributions.png", width = 10, height = 6)

# 3. (Optional) Demonstrate pivot_wider() to return to the original format
# This is how you would use pivot_wider if you had the long data and needed the wide format.
df_wide_original <- df_long %>%
  pivot_wider(
    names_from = shot_type,
    values_from = value
  )



# Check that the wide data matches the original df
# print(all.equal(df, df_wide_original))
print('---- wide format dataframe (reconstructed) ----')
print(df_wide_original) 