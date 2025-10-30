# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_7_SelfJoinBuildWinLoss.R
# DATE 2025-10-13
# DESCRIPTION: 

library(RSQLite)
library(DBI)
library(dplyr)
library(readr)
library(stringr)

# 1. Connect to database
path_to_database <- '/home/stevie/DLUBU/EXAMPLES/DATA/Boxscores/Boxscores.db'

con <- dbConnect(RSQLite::SQLite(), path_to_database)

# # 2. Join Boxscores table with itself. 
# query <- tbl(con, "Boxscores") |> 
#   left_join(tbl(con, "Boxscores"), by = "GAME_ID", suffix = c("_team","_opponent")) |>
#     filter(TEAM_ID_team != TEAM_ID_opponent) #|>
#       # mutate(
#       #   WIN_LOSS_team = case_when(
#       #     SCORE_team > SCORE_opponent ~ 1,
#       #     SCORE_team < SCORE_opponent ~ 0
#       #   )
#       # ) |> 
#       #   mutate(
#       #     WIN_LOSS_opponent = case_when(
#       #       WIN_LOSS_team == 1 ~ 0,
#       #       WIN_LOSS_team == 0 ~ 1
#       #     )
#       #   )
#       #   ) #|> 
#           #select(-ends_with("_opponent")) |>
#             #rename_with(~ str_remove(., "_team"), ends_with("_team"))


query <- tbl(con, "Boxscores") |>
  

# 3. Display the query
show_query(query) 

# 4. Run the query
results_df <- query |>
  collect()

results_df <- results_df |>
  mutate(
         WIN_LOSS_team = case_when(
           SCORE_team > SCORE_opponent ~ 1,
           SCORE_team < SCORE_opponent ~ 0
         )
        ) |> 
          mutate(
            WIN_LOSS_opponent = case_when(
              WIN_LOSS_team == 1 ~ 0,
              WIN_LOSS_team == 0 ~ 1
            )
          )
 
# 6. Put the new data back into the database: overwrite the Boxscores table
# dbWriteTable(
#   con,
#   name = "Boxscores",
#   value = results_df,
#   overwrite = TRUE
# )

write_csv(results_df, "results.csv")

# 7. Disconnect database connection
dbDisconnect(con)


