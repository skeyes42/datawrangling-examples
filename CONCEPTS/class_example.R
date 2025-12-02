library(S7)

Boxscore <- new_class("Boxscore",
  properties = list(
    data = class_data.frame
  ),
  validator = function(self) {
    required_cols <- c("GAME_ID", "TEAM_ID", "PLAYER_ID", "FGM", "FG3M", "FTM")
    missing <- setdiff(required_cols, names(self@data))
    if (length(missing) > 0) {
      paste("Missing required columns:", paste(missing, collapse = ", "))
    }
  }
)

method(print, Boxscore) <- function(x, ...) {
  n_rows <- nrow(x@data)
  n_games <- length(unique(x@data$GAME_ID))
  cat(sprintf("Boxscore: %d rows, %d games\n\n", n_rows, n_games))
  print(x@data)
  invisible(x)
}

box <- Boxscore(data = df)
print(box)