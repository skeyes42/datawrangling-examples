## summarize.R

This R program demonstrates how to perform data aggregation and grouping using the dplyr package, which is a core part of the tidyverse.

The program uses the **native pipe operator** \|\> (introduced in R 4.1.0) to pass data through a sequence of functions.

**1. Data Setup**

It creates a data.frame representing basketball box score data with identifiers (GAME_ID, TEAM_ID, PLAYER_ID) and three statistics: field goals made (FGM), three-pointers made (FG3M), and free throws made (FTM).

**2. Basic Grouping and Summarizing**

The code uses group_by() and summarize() to collapse the data into summary statistics:

**Summary by Team:** Calculates the average FGM, total FGM, and the count of players (n()) for each unique TEAM_ID.

**Summary by Game:** Groups the data by GAME_ID to find the total and average FGM per game.

**3. Multiple Grouping Levels**

The final section demonstrates grouping by multiple variables:

**Hierarchical Grouping:** It groups by both GAME_ID and TEAM_ID to calculate stats for each team within each specific game.

**The .groups Argument:** The code specifies .groups = "drop" to ensure the resulting data frame is a standard, ungrouped data frame. Without this, summarize() by default keeps the data grouped by the first variable (GAME_ID), which can lead to unexpected behavior in later steps.

**Key Functions Used**

| **Function**  | **Purpose**                                                                           |
|---------------|---------------------------------------------------------------------------------------|
| group_by()    | "Split" the data into internal subsets based on column values.                        |
| summarize()   | "Apply" functions to those subsets and "Combine" them into a single row per group.    |
| n()           | A helper function that counts the number of observations (rows) in the current group. |
