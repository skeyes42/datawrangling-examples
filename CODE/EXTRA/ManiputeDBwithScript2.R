# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: ManiputeDBwithScript2.R
# DATE 2025-11-10
# DESCRIPTION: 
# This R program is a Master Orchestration Pipeline. Its job 
# is to provide a graphical interface for a user to select a 
# folder and then automatically run a sequence of seven database 
# and analysis scripts in a specific order.



# R Pipeline Runner
# Executes a series of R scripts in sequence

# Using tcltk (works on Windows, Mac, Linux)
library(tcltk)

chosen_dir <- tk_choose.dir(
  default = getwd(),
  caption = "Select a directory"
)

# Check if user cancelled
if (!is.na(chosen_dir)) {
  print(paste("You selected:", chosen_dir))
  
  # Use it to construct file paths
  file_path <- file.path(chosen_dir, "my_data.csv")
  print(paste("Full path would be:", file_path))
} else {
  print("No directory selected")
  stop()
}

# Define the scripts to run in order
scripts <- c(
  "ManiputeDBwithScript.R",
  "SimpleJoinBoxscores.R",
  "ComputePercentagesPoints.R",
  "SelfJoinBuildWinLoss.R",
  "SummarizeTeamLevel.R",
  "RetrieveBoxscoresTable.R",
  "RetrieveSeason2025Table.R"
)

# Function to run a script with error handling
run_script <- function(script_name) {
  cat("\n========================================\n")
  cat("Running:", script_name, "\n")
  cat("========================================\n")
  
  if (!file.exists(script_name)) {
    stop(paste("Error: Script", script_name, "not found!"))
  }
  
  tryCatch({
    source(script_name, echo = TRUE)
    cat("\n✓ Successfully completed:", script_name, "\n")
    return(TRUE)
  }, error = function(e) {
    cat("\n✗ Error in", script_name, ":\n")
    cat(conditionMessage(e), "\n")
    return(FALSE)
  })
}

# Main execution
cat("Starting R Pipeline\n")
cat("Date/Time:", format(Sys.time(), "%Y-%m-%d %H:%M:%S"), "\n")

# Track execution results
results <- data.frame(
  script = character(),
  status = character(),
  stringsAsFactors = FALSE
)

# Run each script
for (script in scripts) {
  setwd(chosen_dir)
  success <- run_script(script)
  results <- rbind(results, data.frame(
    script = script,
    status = ifelse(success, "SUCCESS", "FAILED")
  ))
  
  # Stop pipeline if a script fails
  if (!success) {
    cat("\n!!! Pipeline stopped due to error !!!\n")
    break
  }
}

# Summary
cat("\n========================================\n")
cat("Pipeline Execution Summary\n")
cat("========================================\n")
print(results)

# Check if all succeeded
all_success <- all(results$status == "SUCCESS")
if (all_success) {
  cat("\n✓ All scripts completed successfully!\n")
} else {
  cat("\n✗ Pipeline completed with errors.\n")
  quit(status = 1)
}