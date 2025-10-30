# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_14_AccessClassDefsEnvVar.py
# DATE 2025-10-20
# DESCRIPTION: 

import os
import sqlite3
import pandas as pd
import sys
import sqlite3

# Set up paths
path_to_examples = os.getenv("EXAMPLES")
if path_to_examples is None:
    raise ValueError("EXAMPLES environment variable is not set.")
    
path_to_library = os.path.join(path_to_examples, "LIBRARY/") # Removed the trailing slash for clarity
path_to_database = os.path.join(path_to_examples, "Boxscores.db")

# Append the directory containing the module to sys.path
sys.path.append(path_to_library)

# Verify the path was added and contains the module
print(f"Adding to sys.path: {path_to_library}")
if os.path.isdir(path_to_library) and "BoxscoresClass.py" in os.listdir(path_to_library):
    print("Verification: BoxscoresClass.py found in the specified path.")
else:
    print("Verification failed: BoxscoresClass.py not found in the path.")

# Import the BoxscoresClass module
from BoxscoresClass import get_boxscores_instance

# Get the boxscores instance and dataframe
boxscoresObject = get_boxscores_instance(path_to_database)
boxscores_df = boxscoresObject.boxscores_dataframe()

print(boxscores_df)

print("Done")
