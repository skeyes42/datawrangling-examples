# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_20_BoxscoresTKinter.py
# DATE 2025-10-20
# DESCRIPTION: 

import tkinter as tk
from tkinter import ttk
import pandas as pd
import os
import sys

class DualListboxApp:
    def __init__(self, root, df1, df2):
        self.root = root
        self.root.title("Dual Listbox Display")
        self.root.geometry("800x500")
        
        self.df1 = df1
        self.df2 = df2
        
        self.create_widgets()
        self.populate_listboxes()
    
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Left listbox frame
        left_frame = ttk.LabelFrame(main_frame, text="DataFrame 1", padding="5")
        left_frame.grid(row=0, column=0, rowspan=2, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        
        # Left listbox with scrollbar
        self.listbox1 = tk.Listbox(left_frame, height=20, width=40)
        scrollbar1 = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.listbox1.yview)
        self.listbox1.config(yscrollcommand=scrollbar1.set)
        
        self.listbox1.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar1.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Right listbox frame
        right_frame = ttk.LabelFrame(main_frame, text="DataFrame 2", padding="5")
        right_frame.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)
        
        # Right listbox with scrollbar
        self.listbox2 = tk.Listbox(right_frame, height=20, width=40)
        scrollbar2 = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.listbox2.yview)
        self.listbox2.config(yscrollcommand=scrollbar2.set)
        
        self.listbox2.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar2.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Bind selection events
        self.listbox1.bind('<<ListboxSelect>>', self.on_select_listbox1)
        self.listbox2.bind('<<ListboxSelect>>', self.on_select_listbox2)
    
    def populate_listboxes(self):
        # Clear existing items
        self.listbox1.delete(0, tk.END)
        self.listbox2.delete(0, tk.END)
        
        # Populate listbox 1 with dataframe 1 rows
        for idx, row in self.df1.iterrows():
            row_str = " | ".join([f"{col}: {val}" for col, val in row.items()])
            self.listbox1.insert(tk.END, row_str)
        
        # Populate listbox 2 with dataframe 2 rows
        for idx, row in self.df2.iterrows():
            row_str = " | ".join([f"{col}: {val}" for col, val in row.items()])
            self.listbox2.insert(tk.END, row_str)
    
    def on_select_listbox1(self, event):
        selection = self.listbox1.curselection()
        if selection:
            index = selection[0]
            print(f"Selected from DataFrame 1 (index {index}):")
            print(self.df1.iloc[index])
            print()
    
    def on_select_listbox2(self, event):
        selection = self.listbox2.curselection()
        if selection:
            index = selection[0]
            print(f"Selected from DataFrame 2 (index {index}):")
            print(self.df2.iloc[index])
            print()

# # Example usage
# if __name__ == "__main__":
    
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
#boxscores_df = boxscores_dataframe(boxscoresObject)
boxscores_df = boxscoresObject.boxscores_dataframe()
    
    # Create sample dataframes
    # df1 = pd.DataFrame({
    #     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    #     'Age': [25, 30, 35, 28, 32],
    #     'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin']
    # })
    
df2 = pd.DataFrame({
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'Price': [1200, 800, 500, 300, 100],
    'Stock': [15, 25, 30, 12, 50]
})

# Create and run the application
root = tk.Tk()
app = DualListboxApp(root, boxscores_df, df2)
root.mainloop()