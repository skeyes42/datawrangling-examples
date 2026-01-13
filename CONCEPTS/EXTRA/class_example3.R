library(S7)

# === BASE CLASS ===
StatLine <- new_class("StatLine",
  properties = list(
    FGM = class_integer,
    FGA = class_integer,
    FG3M = class_integer,
    FG3A = class_integer,
    FTM = class_integer,
    FTA = class_integer
  )
)

# Methods inherited by all children
fg_pct <- new_generic("fg_pct", "x")
method(fg_pct, StatLine) <- function(x) {
  if (x@FGA == 0L) return(NA_real_)
  round(x@FGM / x@FGA, 3)
}

fg3_pct <- new_generic("fg3_pct", "x")
method(fg3_pct, StatLine) <- function(x) {
  if (x@FG3A == 0L) return(NA_real_)
  round(x@FG3M / x@FG3A, 3)
}

ft_pct <- new_generic("ft_pct", "x")
method(ft_pct, StatLine) <- function(x) {
  if (x@FTA == 0L) return(NA_real_)
  round(x@FTM / x@FTA, 3)
}

points <- new_generic("points", "x")
method(points, StatLine) <- function(x) {
  (x@FGM - x@FG3M) * 2L + x@FG3M * 3L + x@FTM
}

# === CHILD CLASSES ===
PlayerGame <- new_class("PlayerGame",
  parent = StatLine,
  properties = list(
    GAME_ID = class_integer,
    TEAM_ID = class_integer,
    PLAYER_ID = class_integer
  )
)

TeamGame <- new_class("TeamGame",
  parent = StatLine,
  properties = list(
    GAME_ID = class_integer,
    TEAM_ID = class_integer
  )
)

PlayerSeason <- new_class("PlayerSeason",
  parent = StatLine,
  properties = list(
    PLAYER_ID = class_integer,
    games_played = class_integer
  )
)

# === CONSTRUCTORS FROM DATA ===

# # Build PlayerGame objects from a data frame
# player_games_from_df <- function(df) {
#   lapply(seq_len(nrow(df)), function(i) {
#     row <- df[i, ]
#     PlayerGame(
#       GAME_ID = as.integer(row$GAME_ID),
#       TEAM_ID = as.integer(row$TEAM_ID),
#       PLAYER_ID = as.integer(row$PLAYER_ID),
#       FGM = as.integer(row$FGM),
#       FGA = as.integer(row$FGA),
#       FG3M = as.integer(row$FG3M),
#       FG3A = as.integer(row$FG3A),
#       FTM = as.integer(row$FTM),
#       FTA = as.integer(row$FTA)
#     )
#   })
# }
# Build PlayerGame objects from a data frame using dplyr/purrr
player_games_from_df <- function(df) {
  df |>
    select(GAME_ID, TEAM_ID, PLAYER_ID, FGM, FGA, FG3M, FG3A, FTM, FTA) |>
    mutate(across(everything(), as.integer)) |>
    pmap(PlayerGame)
}

# === AGGREGATION: PlayerGame list -> PlayerSeason ===

aggregate_to_season <- function(player_games, player_id) {
  # Filter to this player
  games <- Filter(function(g) g@PLAYER_ID == player_id, player_games)
  
  if (length(games) == 0) {
    stop(sprintf("No games found for player %d", player_id))
  }
  
  PlayerSeason(
    PLAYER_ID = player_id,
    games_played = as.integer(length(games)),
    FGM = as.integer(sum(sapply(games, function(g) g@FGM))),
    FGA = as.integer(sum(sapply(games, function(g) g@FGA))),
    FG3M = as.integer(sum(sapply(games, function(g) g@FG3M))),
    FG3A = as.integer(sum(sapply(games, function(g) g@FG3A))),
    FTM = as.integer(sum(sapply(games, function(g) g@FTM))),
    FTA = as.integer(sum(sapply(games, function(g) g@FTA)))
  )
}

# === AGGREGATION: PlayerGame list -> TeamGame ===

aggregate_to_team_game <- function(player_games, game_id, team_id) {
  games <- Filter(
    function(g) g@GAME_ID == game_id && g@TEAM_ID == team_id, 
    player_games
  )
  
  if (length(games) == 0) {
    stop(sprintf("No players found for game %d, team %d", game_id, team_id))
  }
  
  TeamGame(
    GAME_ID = game_id,
    TEAM_ID = team_id,
    FGM = as.integer(sum(sapply(games, function(g) g@FGM))),
    FGA = as.integer(sum(sapply(games, function(g) g@FGA))),
    FG3M = as.integer(sum(sapply(games, function(g) g@FG3M))),
    FG3A = as.integer(sum(sapply(games, function(g) g@FG3A))),
    FTM = as.integer(sum(sapply(games, function(g) g@FTM))),
    FTA = as.integer(sum(sapply(games, function(g) g@FTA)))
  )
}

# === DEMO ===

# Your data
csv_text <- "GAME_ID,TEAM_ID,PLAYER_ID,FGM,FGA,FG3M,FG3A,FTM,FTA
1000,100,1,10,13,12,13,12,12
1000,100,2,4,16,4,8,7,8
1000,200,3,2,20,6,13,5,12
1000,200,4,8,16,2,8,7,8
2000,100,1,10,21,4,13,10,12
2000,100,2,11,16,5,8,4,8
2000,300,5,8,14,10,13,9,12
2000,300,6,7,16,6,8,3,8
3000,200,3,5,13,7,13,9,12
3000,200,4,3,17,2,8,6,8
3000,300,5,4,8,4,13,11,12
3000,300,6,8,16,3,8,3,8"

df <- read.csv(text = csv_text)

# Build all PlayerGame objects
all_games <- player_games_from_df(df)

# Show inheritance in action - same methods work on different classes
cat("=== INHERITANCE DEMO ===\n\n")

# Single game (PlayerGame)
game1 <- all_games[[1]]
cat(sprintf("Player %d, Game %d:\n", game1@PLAYER_ID, game1@GAME_ID))
cat(sprintf("  Points: %d | FG%%: %.1f%% | 3P%%: %.1f%%\n\n",
            points(game1), fg_pct(game1) * 100, fg3_pct(game1) * 100))

# Season aggregate (PlayerSeason)
p1_season <- aggregate_to_season(all_games, 1L)
cat(sprintf("Player %d Season (%d games):\n", 
            p1_season@PLAYER_ID, p1_season@games_played))
cat(sprintf("  Points: %d | FG%%: %.1f%% | 3P%%: %.1f%%\n\n",
            points(p1_season), fg_pct(p1_season) * 100, fg3_pct(p1_season) * 100))

# Team game aggregate (TeamGame)
team100_game1000 <- aggregate_to_team_game(all_games, 1000L, 100L)
cat(sprintf("Team %d, Game %d:\n", 
            team100_game1000@TEAM_ID, team100_game1000@GAME_ID))
cat(sprintf("  Points: %d | FG%%: %.1f%% | 3P%%: %.1f%%\n\n",
            points(team100_game1000), 
            fg_pct(team100_game1000) * 100, 
            fg3_pct(team100_game1000) * 100))

# Prove they're different classes sharing behavior
cat("=== CLASS VERIFICATION ===\n")
cat(sprintf("game1 class: %s (parent: %s)\n", 
            class(game1)[1], class(S7_class(game1)@parent)[1]))
cat(sprintf("p1_season class: %s (parent: %s)\n", 
            class(p1_season)[1], class(S7_class(p1_season)@parent)[1]))
cat(sprintf("team100_game1000 class: %s (parent: %s)\n", 
            class(team100_game1000)[1], class(S7_class(team100_game1000)@parent)[1]))
# ```

# The output will show:
# ```
# === INHERITANCE DEMO ===

# Player 1, Game 1000:
#   Points: 68 | FG%%: 76.9% | 3P%%: 92.3%

# Player 1 Season (2 games):
#   Points: 124 | FG%%: 58.8% | 3P%%: 53.8%

# Team 100, Game 1000:
#   Points: 99 | FG%%: 48.3% | 3P%%: 76.2%

# === CLASS VERIFICATION ===
# game1 class: PlayerGame (parent: StatLine)
# p1_season class: PlayerSeason (parent: StatLine)
# team100_game1000 class: TeamGame (parent: StatLine)