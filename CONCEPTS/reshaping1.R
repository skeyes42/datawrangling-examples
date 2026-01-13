library(dplyr)
library(tidyr)
library(ggplot2)
library(ggpattern)

options(tibble.width = Inf)
options(width = 10000) # <--- Add this to stop the wrapping
sink("reshaping1_output.txt")

# Starting data (long format - one row per player-game)
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

# ===== PIVOT_WIDER: Compare player stats across games =====
# Useful for: trend analysis, game-to-game comparisons, calculating deltas

player_across_games <- df |>
  select(PLAYER_ID, GAME_ID, FGM, FG3M, FTM) |>
  pivot_wider(
    id_cols = PLAYER_ID,
    names_from = GAME_ID,
    values_from = c(FGM, FG3M, FTM),
    names_sep = "_game"
  )

print('---- Pivot Wider Result ----')
print(player_across_games, n = Inf, width = Inf) 

# Now you can easily calculate: FGM improvement, consistency, etc.

player_analysis <- player_across_games |>
  mutate(
    FGM_change = FGM_game2000 - FGM_game1000,
    FG3M_change = FG3M_game2000 - FG3M_game1000
  )

print('---- compute changes between games ----')
print(player_analysis, n = Inf, width = Inf) 

# ===== PIVOT_LONGER: Analyze individual stat contributions =====
# Useful for: comparing stat types within player-game, finding dominant stat

player_stat_breakdown <- df |>
  pivot_longer(
    cols = c(FGM, FG3M, FTM),
    names_to = "stat_type",
    values_to = "value"
  )
print('---- Pivot Longer Result ----')
print(head(player_stat_breakdown))


# Now analyze which stat type dominates for each player across games
player_analysis <- player_stat_breakdown |>
  group_by(PLAYER_ID, stat_type) |>
  summarize(
    avg_value = mean(value),
    total_value = sum(value),
    .groups = "drop"
  ) |>
  arrange(PLAYER_ID, desc(avg_value))

# Or find each player's strongest stat per game
player_analysis <- player_stat_breakdown |>
  group_by(GAME_ID, PLAYER_ID) |>
  slice_max(value, n = 1) |>
  ungroup()

ggplot(player_stat_breakdown, aes(x = stat_type, y = value, 
                                   pattern = stat_type)) +
  geom_col_pattern(
    pattern_fill = "white",
    pattern_color = "black",
    fill = "gray90",
    color = "black"
  ) +
  facet_grid(PLAYER_ID ~ GAME_ID, labeller = label_both) +
  labs(
    title = "Player Performance Breakdown by Game",
    x = "Stat Type",
    y = "Value"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggsave("faceted bar chart.png")

sink()