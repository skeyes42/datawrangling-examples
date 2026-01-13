## chaining.R

1\. Data Initialization

The code uses tribble() create a small dataset (a "tibble") where each row represents a player's performance in a game.

**Columns:** GAME_ID (the specific match), TEAM_ID (the team identifier), PLAYER_ID, and shooting stats (FGM, FG3M, FTM).

2\. Processing Pipeline

The program executes a series of "piped" operations using \|\> to transform the data:

**mutate()**: It creates a new column, TOTAL_PTS, for each player using the formula:

(2×FGM)+(3×FG3M)+FTM

.**group_by()**: It organizes the data into subgroups based on GAME_ID and TEAM_ID. Any following calculation will now happen *per team per game*.

**summarise()**: It reduces each group to a single row by summing all players' TOTAL_PTS into a new column, TEAM_PTS.

.groups = "drop" ensures the resulting data frame is no longer grouped for future steps.

**arrange()**: It sorts the results.

First, it sorts by GAME_ID (ascending).

Then, within each game, it sorts by TEAM_PTS in **descending** order (desc()), effectively putting the winning team (highest scorer) at the top of each game group.

**Summary of Results**

The final output is a table showing the **total points scored by each team in each game**, ranked from highest to lowest score within those games.
