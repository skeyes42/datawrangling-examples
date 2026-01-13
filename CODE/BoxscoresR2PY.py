# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: BoxscoresR2PY.py
# DATE 2025-10-17
# DESCRIPTION: 
# This program is a data pipeline that uses Python as a "wrapper" to 
# execute R code. Its primary purpose is to retrieve complex data 
# structured in R and convert it into a standard Pandas DataFrame for 
# use in Python.

import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter

import os

# Install the S7 package in R via rpy2 ---
# Define the R utility package
utils = importr('utils')

# Define the package to install. rpy2 works by importing R packages.
packnames_to_install = ('S7',)

# Get the list of installed R packages
packages = utils.installed_packages()
package_names = [p for p in packages.rx(True, 1)]

# If S7 is not installed, install it
if 'S7' not in package_names:
    utils.install_packages(ro.StrVector(list(packnames_to_install)))

# Import the S7 package into the rpy2 session
s7 = importr('S7')

# Define and execute the R code ---
# The R code is placed inside a multiline string.

r_file_path = os.getenv("EXAMPLES") + "LIBRARY/" + "BoxscoresClass.R"
try:
    with open(r_file_path, 'r') as file:
        r_code = file.read()
except FileNotFoundError:
  print(f"Error not found: '{r_file_path}'")


# Execute the R code string
ro.r(r_code)

# Access and convert the R data.frame ---
# Activate the pandas conversion context for rpy2
# This ensures R data frames are automatically converted to pandas DataFrames.
with localconverter(ro.default_converter + pandas2ri.converter) as cv:
    # Get the R function from the R environment
    r_function = ro.r['get_Boxscores_data']
    
    # Call the R function. rpy2 handles the R data.frame to pandas conversion.
    df_from_r = r_function()

# --- Step 4: Use the pandas DataFrame in Python ---
print("Type of the object returned from R:", type(df_from_r))
print("\nPandas DataFrame:")
print(df_from_r)

print("Done")

