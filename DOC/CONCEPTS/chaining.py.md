## chaining.py file

This Python program uses the **pandas** library to calculate and rank total team scores from a dataset of individual player statistics.

**Step-by-Step Breakdown**

**1. Data Creation**  
The program initializes a DataFrame (df) representing box score data. Each row contains a game ID, a team ID, a player ID, and their successful shots: Field Goals Made (FGM), 3-Pointers Made (FG3M), and Free Throws Made (FTM).

**2. Calculating Individual Points**

python

.assign(TOTAL_PTS = lambda x: 2\*x['FGM'] + 3\*x['FG3M'] + x['FTM'])

Use code with caution.

It creates a new column, TOTAL_PTS, using a standard basketball scoring formula:

**2 points** for every Field Goal (FGM)

**3 points** for every 3-Pointer (FG3M)

**1 point** for every Free Throw (FTM)

**3. Grouping and Aggregating**

python

.groupby(['GAME_ID', 'TEAM_ID'], as_index=False)

.agg(TEAM_PTS=('TOTAL_PTS', 'sum'))

Use code with caution.

It groups the data by Game and Team, then sums up all the individual TOTAL_PTS to get a single TEAM_PTS value for each team per game.

**4. Sorting the Results**

python

.sort_values(['GAME_ID', 'TEAM_PTS'], ascending=[True, False])

Use code with caution.

The final table is sorted chronologically by GAME_ID (lowest to highest) and then by TEAM_PTS (highest to lowest). This effectively lists the winner of each game first.
