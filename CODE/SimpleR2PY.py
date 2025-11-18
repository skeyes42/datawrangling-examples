# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_17_SimpleR2PY.py
# DATE 2025-10-17
# DESCRIPTION: 

import rpy2.robjects as robjects
import os

import rpy2.robjects as robjects
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage
import os

# Create a sample list of numbers in Python
python_data = [4, 9, 16, 25]

# Path to the R script
script_dir = os.path.dirname(os.path.abspath(__file__))
r_script_path = os.path.join(script_dir, "Example_17a_SimpleR2PY.R")

# Read the R script into a string
with open(r_script_path, 'r') as f:
    r_code = f.read()

# Load the R code into an anonymous package
# This makes the R functions available as Python methods
r_functions = SignatureTranslatedAnonymousPackage(r_code, "r_functions")

# Call the R function with the Python list
# rpy2 automatically converts the Python list to an R vector
r_result = r_functions.process_data(robjects.FloatVector(python_data))

# The result is an R object. Convert it back to a Python list.
python_result = list(r_result)

print(f"Python input data: {python_data}")
print(f"Result from R: {python_result}")

print("Done")

