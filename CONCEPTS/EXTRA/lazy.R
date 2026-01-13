# R: Lazy evaluation in function arguments and some dplyr operations
library(dplyr)
library(tibble)

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

# Example 1: Lazy evaluation in function arguments
demonstrate_lazy <- function(x, y) {
  cat("Function called\n")
  if (x > 5) {
    cat("Returning x, y never evaluated\n")
    return(x)
  }
  cat("Now evaluating y\n")
  x + y
}

# This succeeds - stop() never executes because y is never needed
result1 <- demonstrate_lazy(10, stop("This would error!"))
cat("Result:", result1, "\n\n")

# Example 2: Row-wise operations show evaluation differences
cat("=== R: mutate evaluates expressions ===\n")
system.time({
  r_result <- df %>%
    mutate(
      POINTS = FGM * 2 + FG3M * 3 + FTM,  # Evaluated immediately
      HEAVY_CALC = {
        Sys.sleep(0.01)  # Simulate expensive operation
        POINTS * 2
      }
    ) %>%
    filter(POINTS > 30)  # Even filtered-out rows calculated HEAVY_CALC
})

# Example 3: Lazy evaluation with summarize
cat("\n=== R: Grouped operations ===\n")
system.time({
  team_stats <- df %>%
    group_by(TEAM_ID) %>%
    summarise(
      total_fgm = sum(FGM),
      # This expensive calc only runs once per group, not per row
      adjusted_score = {
        Sys.sleep(0.01)
        sum(FGM * 2 + FG3M * 3 + FTM)
      }
    )
})
print(team_stats)