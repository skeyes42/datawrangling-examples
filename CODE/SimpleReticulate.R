# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_15_SimpleReticulate.R
# DATE 2025-10-15
# DESCRIPTION: 

library(reticulate)

py_install(c("nba_api", "pandas"))

py_config()

pandas_module <- reticulate::import("pandas")
nba_api       <- reticulate::import("nba_api")

# Source the Python script
reticulate::source_python("Example_15_SimpleReticulate.py")

lebron_id <- get_player_id("LeBron James")

print(lebron_id)
