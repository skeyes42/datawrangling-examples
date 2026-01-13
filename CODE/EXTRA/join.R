library(RSQLite)
library(DBI)
library(dplyr)
library(dbplyr)
library(readr)

path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")

# Connect to database
con <- dbConnect(RSQLite::SQLite(), path_to_database)

# Bring into Boxscores the player and team names
query <- tbl(con, "Boxscores") |>
  left_join(tbl(con, "Teams"), by = "TEAM_ID") |>
  left_join(tbl(con, "Players"), by = "PLAYER_ID") 
  
# Display the query
show_query(query)

# Run the query
results_df <- query |>
  collect()

# Disconnect database connection
dbDisconnect(con)

# Review results of join
print(results_df, width = Inf)