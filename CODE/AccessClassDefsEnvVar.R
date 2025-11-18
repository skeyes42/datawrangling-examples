# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_14_AccessClassDefsEnvVar.R
# DATE 2025-10-16
# DESCRIPTION: 

# Set up the paths
path_to_library  <- paste0(Sys.getenv("EXAMPLES"), "LIBRARY/")
path_to_database <- paste0(Sys.getenv("EXAMPLES"), "Boxscores.db")

# Get Boxscores class from library
source(paste0(path_to_library, "BoxscoresClass.R"))

# Instantiate the Boxscores class
boxscoresObject <- get_Boxscores_instance(path_to_database)

# Get Boxscores data
boxscores_df <- boxscores_dataframe(boxscoresObject)

print(boxscores_df)
