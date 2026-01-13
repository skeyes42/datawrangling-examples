# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: SimpleReticulate.R
# DATE 2025-10-15
# DESCRIPTION: 
# This R program demonstrates a sophisticated use of the reticulate 
# library to integrate Python capabilities directly into an R 
# environment. It specifically sets up a workspace to interact with 
# NBA data using Python's nba_api.


library(reticulate)

py_install(c("nba_api", "pandas"))

py_config()

pandas_module <- reticulate::import("pandas")
nba_api       <- reticulate::import("nba_api")

# Source the Python script
reticulate::source_python("SimpleReticulate.py")

lebron_id <- get_player_id("LeBron James")

print(lebron_id)
