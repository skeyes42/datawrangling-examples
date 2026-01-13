# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: AccessClassDefsEnvVar.R
# DATE 2025-10-16
# DESCRIPTION: 
# This R program demonstrates object-oriented programming (OOP) 
# principles and modularity. It uses a custom-built "class" system 
# to fetch basketball data from a database.

# Set up the paths
path_to_library  <- file.path(Sys.getenv("EXAMPLES"), "LIBRARY/")
path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")

# Get Boxscores class from library
source(paste0(path_to_library, "BoxscoresClass.R"))

# Instantiate the Boxscores class
boxscoresObject <- get_Boxscores_instance(path_to_database)

# Get Boxscores data
boxscores_df <- boxscores_dataframe(boxscoresObject)

print(boxscores_df)
