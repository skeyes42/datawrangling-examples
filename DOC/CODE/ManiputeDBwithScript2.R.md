## ManiputeDBwithScript2.R

This R program is a **Master Orchestration Pipeline**. Its job is to provide a graphical interface for a user to select a folder and then automatically run a sequence of seven database and analysis scripts in a specific order.

Here is the breakdown of how it works in 2026:

**1. Graphical Directory Selection**

The program uses the tcltk library to open a standard folder-selection window on your computer.

**User Choice**: It asks you to "Select a directory."

**Safety Check**: If you click "Cancel," the program prints a warning and stops immediately (stop()) to prevent errors.

**Pathing**: Once a folder is chosen, it sets that as the "Home" for all subsequent operations.

**2. The Workflow (The Script Queue)**

The program defines a specific sequence of scripts (scripts \<- c(...)) to execute. Based on their names, this pipeline follows a logical data science lifecycle:

**Preparation**: ManiputeDBwithScript.R (likely sets up the database).

**Joining**: SimpleJoinBoxscores.R (combines tables).

**Calculation**: ComputePercentagesPoints.R (adds stats).

**Logic Building**: SelfJoinBuildWinLoss.R (determines who won/lost).

**Aggregation**: SummarizeTeamLevel.R (groups data by team).

**Extraction**: RetrieveBoxscoresTable.R and RetrieveSeason2025Table.R (exports final results).

**3. Robust Execution with Error Handling**

The core of the program is the run_script function, which uses a tryCatch block. This is a "safety net" that does two things:

**Success**: If a script works, it prints a green checkmark (✓) and moves to the next one.

**Failure**: If a script crashes, it catches the error, prints a red "X" (✗), explains what went wrong, and **stops the entire pipeline**. This prevents "cascading errors" where a later script tries to use data that a failed earlier script never created.

**4. Reporting and Monitoring**

As the pipeline runs, it generates a real-time log:

**Timestamping**: It logs exactly when the pipeline started using the 2026 date/time format.

**Tracking**: It builds a small table (results) that keeps track of which scripts passed and which failed.

**Summary**: Once finished, it prints a final "Pipeline Execution Summary" table so you can see the status of all seven scripts at a glance.

**Summary of Utility**

This is a **Control Script**. Instead of a user having to manually open and run seven different files in the correct order, they simply run this one program, select their data folder, and let the automation handle the rest. It ensures that the 2026 season data is processed consistently and correctly every time.
