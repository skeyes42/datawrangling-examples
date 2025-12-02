# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_16_BoxscoresReticulate.R
# DATE 2025-10-17
# DESCRIPTION: 


# R script to call the Python function

# Load the reticulate library
library(reticulate)

# Source the Python script containing the getBoxscores function
# Make sure the file path is correct for your system.
source_python("BoxscoresReticulate.py")

# Define the database and table names.
# Adjust the file path to point to your database.
db <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")
table <- 'Boxscores'

# Call the Python function.
# The result will be an R data frame due to reticulate's automatic conversion.
boxscores_df_r <- getBoxscores(db, table)

# Check the class of the returned object to confirm it's an R data frame
print(class(boxscores_df_r))

# Print the first few rows of the data frame
if (!is.null(boxscores_df_r)) {
  print(head(boxscores_df_r))
} else {
  print("Failed to retrieve data. Check the Python function and database path.")
}

print("Done")
