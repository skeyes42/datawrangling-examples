# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: FunctionToManiputeDB.py
# DATE 2025-10-26
# DESCRIPTION:
# This Python program is a database administration script designed to 
# completely reset a SQLite database to a known, empty state. It uses 
# the operating system's command line to execute SQL scripts, 
# demonstrating a powerful way to manage database structure.

import os
import sqlite3
import subprocess

def flush_database(path_to_scripts):
    """
    Function to drop all tables and recreate them using SQL scripts.
    """
    db_path = os.path.join(path_to_scripts, "Boxscores.db")

    # Command to drop all tables
    drop_command = f".read drop_all_tables.sql"
    try:
        subprocess.run(["sqlite3", db_path], 
                       input=drop_command.encode('utf-8'), 
                       check=True, 
                       cwd=path_to_scripts)
    except subprocess.CalledProcessError as e:
        print(f"Error dropping tables: {e}")
        return
        
    # Command to recreate tables
    recreate_command = f".read boxscores.sql"
    try:
        subprocess.run(["sqlite3", 
                        db_path], input=recreate_command.encode('utf-8'), 
                       check=True, 
                       cwd=path_to_scripts)
    except subprocess.CalledProcessError as e:
        print(f"Error recreating tables: {e}")
        return

def db_list_tables(con):
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    return tables

# Setup path_to_scripts
path_to_scripts = os.getenv("EXAMPLES")

if not path_to_scripts or not os.path.isdir(path_to_scripts):
    print("Environment variable 'EXAMPLES' is not set ")
    exit()

# Flush the database using the function
flush_database(path_to_scripts)

# Create connection to database
path_to_database = os.path.join(path_to_scripts, "Boxscores.db")
con = sqlite3.connect(path_to_database)

# Get list of tables after flushing
before = db_list_tables(con)
print('--- tables after flush_database() ---')
print(before)

# Demonstrate dropping tables manually
print('\n--- manually dropping tables ---')
drop_command = ".read drop_all_tables.sql"
try:
    subprocess.run(["sqlite3", path_to_database], 
                   input=drop_command.encode('utf-8'), 
                   check=True, 
                   cwd=path_to_scripts)
except subprocess.CalledProcessError as e:
    print(f"Error dropping tables manually: {e}")

# Get list of tables after dropping
after_dropping = db_list_tables(con)
print('--- after dropping ---')
print(after_dropping)

# Demonstrate recreating tables manually
print('\n--- manually recreating tables ---')
recreate_command = ".read boxscores.sql"
try:
    subprocess.run(["sqlite3", path_to_database], 
                   input=recreate_command.encode('utf-8'), 
                   check=True, 
                   cwd=path_to_scripts)
except subprocess.CalledProcessError as e:
    print(f"Error recreating tables manually: {e}")

# Get list of tables after recreation
after_recreating = db_list_tables(con)
print('--- after recreating ---')
print(after_recreating)

# Disconnect from database
con.close()
print("\nDone")

