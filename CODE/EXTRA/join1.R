library(RSQLite)
library(DBI)
library(dplyr)


path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")

# Connect to database
con <- dbConnect(RSQLite::SQLite(), path_to_database)

query <- tbl(con, "Boxscores") |>
  left_join(tbl(con, "Players"), by = "PLAYER_ID") |>
  left_join(tbl(con, "Teams"), by = "TEAM_ID")

results_df <- collect(query)
print(colnames(results_df))

# Check if TEAM_NAME has data
print(results_df$TEAM_NAME)

# Check if PLAYER_NAME has data
print(results_df$PLAYER_NAME)

dbDisconnect(con)