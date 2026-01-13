library(tidyverse)
library(RSQLite)

# Connect to database with error handling
path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")
 
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Bring into Boxscores the player and team names
query <- tbl(con, "Boxscores")                     |>
  left_join(tbl(con, "Players"), by = "PLAYER_ID") |>
    left_join(tbl(con, "Teams"), by = "TEAM_ID")   |>
        arrange(GAME_ID, TEAM_ID)                  |>
          select(-PLAYER_ID, -TEAM_ID)             |>
            as_tibble() 
           

# Run the query
shooting <- query |>
  collect()

print(shooting)

dbDisconnect(con)

# Pivot longer to stack all shot types
shooting_long <- shooting |>
  pivot_longer(
    cols = c(FGM, FGA, FG3M, FG3A, FTM, FTA),
    names_to = "stat_type",
    values_to = "count"
  )

# Calculate shooting percentages by player
shooting_summary <- shooting_long |>
  separate(stat_type, into = c("shot_type", "made_attempt"), sep = -1) |>
  pivot_wider(
    names_from = made_attempt,
    values_from = count,
    values_fn = sum
  ) |>
  mutate(pct = M / A * 100) |>
  group_by(PLAYER_NAME, shot_type) |>
  summarise(
    total_attempts = sum(A),
    shooting_pct = mean(pct, na.rm = TRUE),
    .groups = "drop"
  )

print(shooting_summary)