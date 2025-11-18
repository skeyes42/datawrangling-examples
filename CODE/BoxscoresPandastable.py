# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_19_BoxscoresPandastable.py
# DATE 2025-10-17
# DESCRIPTION: 

from tkinter import *
import pandas as pd
from pandastable import Table, TableModel

import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter

import os

# Setup package environment
utils = importr('utils')
packnames_to_install = ('S7',)
packages = utils.installed_packages()
package_names = [p for p in packages.rx(True, 1)]
if 'S7' not in package_names:
    utils.install_packages(ro.StrVector(list(packnames_to_install)))
s7 = importr('S7')

# Get the R Boxscores class
r_file_path = os.getenv("EXAMPLES") + "LIBRARY/" + "BoxscoresClass.R"
try:
    with open(r_file_path, 'r') as file:
        r_code = file.read()
except FileNotFoundError:
  print(f"Error not found: '{r_file_path}'")

# Call the R class function to get Boxscores dataframe. Convert to Panda
ro.r(r_code)
with localconverter(ro.default_converter + pandas2ri.converter) as cv:
    r_function = ro.r['get_Boxscores_data']
    df_from_r = r_function()

# Class to setup TKinter environment for pandastable
class DataFrameViewer(Frame):
    def __init__(self, parent, dataframe):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack(fill=BOTH, expand=True)

        self.table = pt = Table(self, dataframe=dataframe,
                                showtoolbar=True, showstatusbar=True)
        pt.show()

 # Create the Tkinter root window
root = Tk()
root.title("Pandas DataFrame Viewer")
root.geometry("600x400") # Set initial window size

# Create an instance of the DataFrameViewer
viewer = DataFrameViewer(root, df_from_r)

# Start the Tkinter event loop
root.mainloop()