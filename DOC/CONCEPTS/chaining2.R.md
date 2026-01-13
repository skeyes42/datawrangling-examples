## chaining2.R

Chain friendly funcitons

Step-by-Step Breakdown

1\. Data Initialization (tibble::tribble)  
The program creates a "tibble" (an enhanced data frame) containing columns for Game ID, Team ID, Player ID, and shot statistics:

FGM: Total Field Goals Made.

FG3M: 3-Point Field Goals Made.

FTM: Free Throws Made.

2\. Custom Scoring Function (calc_points)

calc_points \<- function(fgm, fg3m, ftm) {

(fgm - fg3m) \* 2 + fg3m \* 3 + ftm

Use code with caution.

This function calculates individual player points. It subtracts 3-pointers from total field goals to isolate 2-pointers (multiplied by 2), then adds the 3-pointers (multiplied by 3) and free throws (multiplied by 1).

3\. The Data Pipeline (\|\>)  
The program uses the native R pipe operator \|\> to pass the data through a series of transformations:

mutate(): Applies the calc_points function to every row, creating a new column called PTS.

group_by(): Organizes the data by GAME_ID and TEAM_ID so that subsequent calculations are performed per team, per game.

summarize(): Sums up the PTS for all players on the same team in a specific game to create a new variable, TEAM_PTS.

.groups = "drop": Ensures the final result is a standard, ungrouped table for easier use in later steps.
