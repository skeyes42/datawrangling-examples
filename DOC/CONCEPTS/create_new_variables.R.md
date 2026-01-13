## create_new_variables.R

Core Data: boxscores_df

The program starts with a standard R data.frame containing basketball statistics: GAME_ID, TEAM_ID, PLAYER_ID, and various shot types (FGM, FG3M, FTM).

1\. mutate(): Adding a New Column (First Example)

r

boxscores_updated_df \<- boxscores_df \|\>

mutate(SCORING_EFFORT = FGM + FG3M + FTM)

Use code with caution.

Purpose: mutate() creates a new column while keeping all existing columns.

Action: It calculates a simple sum of all successful shots (FGM + FG3M + FTM) and stores it in the new column SCORING_EFFORT.

Output (excerpt): The resulting data frame includes all original columns plus the new SCORING_EFFORT column.

2\. transmute(): Keeping Only New Columns

r

boxscores_updated_df \<- boxscores_df \|\>

transmute(SCORING_EFFORT = FGM + FG3M + FTM)

Use code with caution.

Purpose: transmute() creates a new column (or columns) but drops all original columns by default.

Action: It performs the same calculation as the first example, but the output data frame will *only* contain the new SCORING_EFFORT column.

Output (excerpt): A data frame with a single column: SCORING_EFFORT.

3\. mutate(across()): Applying a Function to Multiple Columns

r

boxscores_updated_df \<- boxscores_df \|\>

mutate(across(c(FGM, FG3M, FTM), \~ .x \* 2, .names = "{.col}_doubled"))

Use code with caution.

Purpose: mutate(across()) efficiently applies the same function to a selection of columns.

Action:

c(FGM, FG3M, FTM) selects these three specific columns.

\~ .x \* 2 defines an anonymous function (using the "formula syntax" \~) that multiplies the value in each column (.x) by 2.

.names = "{.col}_doubled" is a naming convention: it creates new columns with the original name appended with \_doubled (e.g., FGM_doubled).
