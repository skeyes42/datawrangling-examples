## self_join1.R

This R program uses the **dplyr** and **tidyr** libraries to analyze basketball statistics by employing a powerful data manipulation technique called a **self-join**.

The goal is to move beyond individual player stats and analyze the relationships and performance gaps *between teammates* within the same game.

**How the Program Works**

The script follows several key steps:

**1. Setup and Data Creation**

It creates a sample dataset called boxscores that lists individual player statistics (FGM, FGA, etc.) for several different games (GAME_ID) and teams (TEAM_ID).

**2. The Core Logic: Self-Join**

The crucial step is the inner_join(boxscores, boxscores, by = c("GAME_ID", "TEAM_ID")).

**Joining on two keys** ensures that rows only match up if they occurred in the *exact same game* AND for the *exact same team*. This isolates players who were teammates.

**Suffixes** (_p1, \_p2) are added to column names to distinguish the "first player's" stats from the "second player's" stats in the resulting table.

**3. Filtering and Cleaning**

The initial self-join produces two unwanted results:

A player matched with themselves (Fred matched with Fred).

Duplicate pairs (Fred, John) and (John, Fred).

The line filter(PLAYER_ID_p1 \< PLAYER_ID_p2) cleverly removes both issues, leaving a clean list of unique two-player combinations per game.

**4. Analysis: Scoring Differential**

The code calculates total points for each player in the pair and then determines the absolute difference (PTS_diff). This metric shows the scoring gap between the two teammates.

**5. Summary**

Finally, the script groups the results by TEAM_ID to calculate the *average* scoring gap across all games.

**Program Output & Insights**

The final output team_balance provides a summary of which teams have an even distribution of scoring versus those that rely heavily on one "star" player:

Team Scoring Balance (lower gap = more balanced):

\# A tibble: 3 × 4

TEAM_ID games_played avg_teammate_gap max_teammate_gap

\<dbl\> \<int\> \<dbl\> \<dbl\>

1 300 2 7.5 8

2 100 2 9 10

3 200 2 11.5 16

**Interpretation:** Team 300 has the smallest average scoring gap (7.5 points) between its teammates, suggesting it has the most balanced scoring distribution among the three teams analyzed. Team 200 is the most reliant on a "star," with an average gap of 11.5 points.
