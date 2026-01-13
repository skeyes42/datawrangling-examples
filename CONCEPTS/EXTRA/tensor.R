# Install and load torch
# install.packages("torch")
library(torch)
library(dplyr)
library(tidyr)

# Sample Data Frame similar to example_data_full.R
# --- Boxscores data --------------------------------------------------
df <- data.frame(
  GAME_ID = c(1000, 1000, 1000, 1000, 2000, 2000, 2000, 
              2000, 2000, 3000, 3000, 3000),
  TEAM_ID = c(100, 100, 200, 200, 100, 100, 300, 300, 
              200, 200, 200, 300),
  PLAYER_ID = c(1, 2, 3, 4, 1, 2, 5, 6, 3, 4, 5, 6),
  FGM  = c(10, 4, 2, 8, 10, 11, 8, 7, 5, 3, 4, 8),
  FGA  = c(13, 16, 20, 16, 21, 16, 14, 16, 13, 17, 8, 16),
  FG3M = c(12, 4, 6, 2, 4, 5, 10, 6, 7, 2, 4, 3),
  FG3A = c(13, 8, 13, 8, 13, 8, 13, 8, 13, 8, 13, 8),
  FTM  = c(12, 7, 5, 7, 10, 4, 9, 3, 9, 6, 11, 3),
  FTA  = c(12, 8, 12, 8, 12, 8, 12, 8, 12, 8, 12, 8)
)



# 1. Prepare the data
# We select the numeric features and group them by GAME_ID
# To create a uniform tensor, we'll take the top 2 players per game (for this example)
df_tensor_prep <- df %>%
  group_by(GAME_ID) %>%
  slice_head(n = 2) %>% # Keep top 2 players per game for symmetry
  ungroup() %>%
  select(FGM, FGA, FG3M, FG3A, FTM, FTA)

# 2. Convert Data Frame to a 2D Matrix first
data_matrix <- as.matrix(df_tensor_prep)

# 3. Create the Tensor
# Basic 2D Tensor
boxscore_tensor <- torch_tensor(data_matrix)

# 4. Reshape into 3D (Games, Players per Game, Features)
# Your data has 3 games, 2 players selected per game, and 6 stats
reshaped_tensor <- boxscore_tensor$view(c(3, 2, 6))

# Print Results
print("Tensor Shape (Games, Players, Stats):")
print(reshaped_tensor$shape)

print("Data for Game 1 (all players and stats):")
print(reshaped_tensor[1, , ])

