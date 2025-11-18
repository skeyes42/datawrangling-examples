# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_20_BoxscoresTKinter.py
# DATE 2025-10-20
# DESCRIPTION: 

import tkinter as tk
from tkinter import ttk
import pandas as pd
import os
import sys

class TripleListboxApp:
    def __init__(self, root, df1, df2, df3):
        self.root = root
        self.root.title("Triple Listbox Display")
        self.root.geometry("800x500")
        
        self.df1 = df1
        self.df2 = df2
        self.df3 = df3
        
        self.create_widgets()
        self.populate_listboxes()
    
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, 
                        sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        #############################################
        # Left listbox frame
        left_frame = ttk.LabelFrame(main_frame, text="DataFrame 1", 
                                    padding="5")
        left_frame.grid(
            row=0, column=0, rowspan=2, padx=5, pady=5, 
            sticky=(tk.W, tk.E, tk.N, tk.S))
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        
        # Left listbox with scrollbar
        self.listbox1 = tk.Listbox(left_frame, height=20, width=40)
        scrollbar1 = ttk.Scrollbar(
            left_frame, orient=tk.VERTICAL, command=self.listbox1.yview)
        self.listbox1.config(yscrollcommand=scrollbar1.set)
        
        self.listbox1.grid(row=0, column=0, 
                           sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar1.grid(row=0, column=1, 
                        sticky=(tk.N, tk.S))

        ############################################
        # middle listbox frame
        middle_frame = ttk.LabelFrame(main_frame, text="DataFrame 2", 
                                      padding="5")
        middle_frame.grid(
            row=0, column=1, rowspan=2, padx=5, pady=5, 
            sticky=(tk.W, tk.E, tk.N, tk.S))
        middle_frame.columnconfigure(0, weight=1)
        middle_frame.rowconfigure(0, weight=1)
        
        # middle listbox with scrollbar
        self.listbox2 = tk.Listbox(middle_frame, height=20, width=40)
        scrollbar2 = ttk.Scrollbar(
            middle_frame, orient=tk.VERTICAL, command=self.listbox2.yview)
        self.listbox2.config(yscrollcommand=scrollbar2.set)
        
        self.listbox2.grid(row=0, column=0, 
                           sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar2.grid(row=0, column=2, sticky=(tk.N, tk.S))
        
        
        ##############################################
        # Right listbox frame
        right_frame = ttk.LabelFrame(main_frame, text="DataFrame 3", 
                                     padding="5")
        right_frame.grid(
            row=0, column=4, rowspan=2, padx=5, pady=5, 
            sticky=(tk.W, tk.E, tk.N, tk.S))
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)
        
        # Right listbox with scrollbar
        self.listbox3 = tk.Listbox(right_frame, height=20, width=40)
        scrollbar3 = ttk.Scrollbar(
            right_frame, orient=tk.VERTICAL, command=self.listbox3.yview)
        self.listbox3.config(yscrollcommand=scrollbar3.set)
        
        self.listbox3.grid(row=0, column=0, 
                           sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar3.grid(row=0, column=4, sticky=(tk.N, tk.S))
        
        ################################################
        # Bind selection events
        self.listbox1.bind('<<ListboxSelect>>', self.on_select_listbox1)
        self.listbox2.bind('<<ListboxSelect>>', self.on_select_listbox2)
        self.listbox3.bind('<<ListboxSelect>>', self.on_select_listbox3)
    
    def populate_listboxes(self):
        # Clear existing items
        self.listbox1.delete(0, tk.END)
        self.listbox2.delete(0, tk.END)
        self.listbox3.delete(0, tk.END)
        
        # Populate listbox 1 with dataframe 1 rows
        first_col_name = self.df1.columns[0]
        for idx, row in self.df1.iterrows():
            value = str(row[first_col_name])
            self.listbox1.insert(tk.END, "Game ID: " + value)
        
        # Populate listbox 2 with dataframe 2 rows
        for idx, row in self.df2.iterrows():
            row_str = " | ".join([f"{col}: {val}" for col, 
                                  val in row.items()])
            self.listbox2.insert(tk.END, row_str)
            
        # Populate listbox 3 with dataframe 3 rows
        for idx, row in self.df3.iterrows():
            row_str = " | ".join([f"{col}: {val}" for col, 
                                  val in row.items()])
            self.listbox3.insert(tk.END, row_str)
    
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
            
    def on_select_listbox3(self, event):
        selection = self.listbox3.curselection()
        if selection:
            index = selection[0]
            print(f"Selected from DataFrame 3 (index {index}):")
            print(self.df3.iloc[index])
            print()


# Example usage
if __name__ == "__main__":
    
    # Get paths
    path_to_examples = os.getenv("EXAMPLES")
    path_to_library = os.path.join(path_to_examples, "LIBRARY/")
    path_to_database = os.path.join(path_to_examples, "Boxscores.db")
    
    # Append the directory containing the module to sys.path
    sys.path.append(path_to_library)
    
    #-------------------------------------------------------
    # Import the BoxscoresClass module
    from BoxscoresClass import get_boxscores_instance
    
    # Get the boxscores instance and dataframe
    boxscoresObject = get_boxscores_instance(path_to_database)
    boxscores_df = boxscoresObject.boxscores_dataframe()
    
    #-------------------------------------------------------
    # Import the PlayersClass module
    from PlayersClass import get_Players_instance
    
    # Get the players instance and dataframe
    playersObject = get_Players_instance(path_to_database)
    players_df = playersObject.players_dataframe()
    
     #-------------------------------------------------------
    # Import the TeamsClass module
    from TeamsClass import get_Teams_instance
    
    # Get the teams instance and dataframe
    teamsObject = get_Teams_instance(path_to_database)
    teams_df = teamsObject.teams_dataframe()
    
    # Create and run the application
    root = tk.Tk()
    app = TripleListboxApp(root, boxscores_df, players_df, teams_df)
    root.mainloop()