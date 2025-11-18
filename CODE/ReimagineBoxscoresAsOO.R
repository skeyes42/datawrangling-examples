library(dplyr)
library(tibble)

# Sample flat boxscore data
boxscore_data <- tibble(
  game_id = c(rep("G001", 10)),
  game_date = c(rep("2024-11-01", 10)),
  home_team = c(rep("Lakers", 10)),
  away_team = c(rep("Warriors", 10)),
  team = c(rep("Lakers", 5), rep("Warriors", 5)),
  player_name = c("LeBron James", "Anthony Davis", "Austin Reaves", 
                  "D'Angelo Russell", "Rui Hachimura",
                  "Stephen Curry", "Klay Thompson", "Draymond Green",
                  "Andrew Wiggins", "Kevon Looney"),
  minutes_played = c(36, 34, 28, 26, 22, 38, 32, 30, 28, 20),
  points = c(28, 24, 14, 12, 8, 32, 22, 8, 16, 6),
  field_goals_made = c(10, 9, 5, 4, 3, 12, 8, 3, 6, 2),
  field_goals_attempted = c(20, 16, 10, 10, 6, 22, 16, 7, 12, 4),
  three_pointers_made = c(2, 0, 2, 2, 0, 6, 4, 0, 2, 0),
  three_pointers_attempted = c(6, 1, 5, 6, 1, 12, 10, 2, 5, 0),
  free_throws_made = c(6, 6, 2, 2, 2, 2, 2, 2, 2, 2),
  free_throws_attempted = c(8, 8, 2, 2, 3, 2, 2, 3, 3, 2),
  rebounds = c(8, 12, 5, 3, 6, 5, 4, 10, 6, 8),
  assists = c(7, 3, 6, 5, 1, 8, 3, 7, 2, 1),
  steals = c(1, 1, 2, 1, 0, 2, 1, 2, 1, 0),
  blocks = c(1, 2, 0, 0, 1, 0, 0, 1, 0, 2),
  turnovers = c(3, 2, 1, 2, 1, 2, 1, 3, 2, 1)
)

# Define Player class constructor
Player <- function(name, minutes, points, fgm, fga, tpm, tpa, ftm, fta, 
                   reb, ast, stl, blk, tov) {
  structure(
    list(
      name = name,
      minutes_played = minutes,
      points = points,
      field_goals_made = fgm,
      field_goals_attempted = fga,
      three_pointers_made = tpm,
      three_pointers_attempted = tpa,
      free_throws_made = ftm,
      free_throws_attempted = fta,
      rebounds = reb,
      assists = ast,
      steals = stl,
      blocks = blk,
      turnovers = tov
    ),
    class = "Player"
  )
}

# Define Team class constructor
Team <- function(name, players) {
  structure(
    list(
      name = name,
      players = players
    ),
    class = "Team"
  )
}

# Define Game class constructor
Game <- function(game_id, date, home_team, away_team) {
  structure(
    list(
      game_id = game_id,
      date = date,
      home_team = home_team,
      away_team = away_team
    ),
    class = "Game"
  )
}

# Transform flat data into nested OO structure
create_game_object <- function(data, game_id_filter) {
  game_data <- data %>% filter(game_id == game_id_filter)
  
  # Extract game metadata
  game_meta <- game_data %>% 
    slice(1) %>% 
    select(game_id, game_date, home_team, away_team)
  
  # Create home team with players
  home_players <- game_data %>%
    filter(team == game_meta$home_team) %>%
    rowwise() %>%
    summarise(
      player_obj = list(Player(
        player_name, minutes_played, points, 
        field_goals_made, field_goals_attempted,
        three_pointers_made, three_pointers_attempted,
        free_throws_made, free_throws_attempted,
        rebounds, assists, steals, blocks, turnovers
      ))
    ) %>%
    pull(player_obj)
  
  home_team_obj <- Team(game_meta$home_team, home_players)
  
  # Create away team with players
  away_players <- game_data %>%
    filter(team == game_meta$away_team) %>%
    rowwise() %>%
    summarise(
      player_obj = list(Player(
        player_name, minutes_played, points,
        field_goals_made, field_goals_attempted,
        three_pointers_made, three_pointers_attempted,
        free_throws_made, free_throws_attempted,
        rebounds, assists, steals, blocks, turnovers
      ))
    ) %>%
    pull(player_obj)
  
  away_team_obj <- Team(game_meta$away_team, away_players)
  
  # Create game object
  Game(game_meta$game_id, game_meta$game_date, home_team_obj, away_team_obj)
}

# Create the game object
game <- create_game_object(boxscore_data, "G001")

# Print methods for better display
print.Player <- function(x, ...) {
  cat(sprintf("%s: %d pts, %d reb, %d ast in %d min\n", 
              x$name, x$points, x$rebounds, x$assists, x$minutes_played))
}

print.Team <- function(x, ...) {
  cat(sprintf("\n%s (%d players):\n", x$name, length(x$players)))
  cat("-------------------\n")
  for (player in x$players) {
    print(player)
  }
}

print.Game <- function(x, ...) {
  cat(sprintf("Game %s - %s\n", x$game_id, x$date))
  cat(sprintf("%s vs %s\n", x$home_team$name, x$away_team$name))
  cat("\nHome Team:")
  print(x$home_team)
  cat("\nAway Team:")
  print(x$away_team)
}

# Display the game
print(game)

# Access examples:
cat("\n\n=== Access Examples ===\n")
cat(sprintf("Game ID: %s\n", game$game_id))
cat(sprintf("Home team: %s\n", game$home_team$name))
cat(sprintf("First home player: %s\n", game$home_team$players[[1]]$name))
cat(sprintf("First home player points: %d\n", game$home_team$players[[1]]$points))
cat(sprintf("Away team leader: %s with %d points\n", 
            game$away_team$players[[1]]$name,
            game$away_team$players[[1]]$points))