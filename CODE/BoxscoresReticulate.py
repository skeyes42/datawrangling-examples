# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: BoxscoresReticulate.py
# DATE 2025-10-16
# DESCRIPTION: 
# This program defines a specialized Python function, getBoxscores, 
# designed to safely extract data from a SQLite database and convert 
# it into a Pandas DataFrame.


import sqlite3
import pandas as pd
import os

def getBoxscores(dbname, table_name):

    # The 'with' statement ensures the connection is properly closed
    try:
        with sqlite3.connect(dbname) as conn:
            # Construct the SQL query to select all data frome table
            query = f"SELECT * FROM {table_name}"
            
            # Use pandas.read_sql_query to execute query and load data
            df = pd.read_sql_query(query, conn)
            
    except sqlite3.Error as e:
        return None
    except pd.io.sql.DatabaseError as e:
        return None
    except FileNotFoundError:
        return None
    except Exception as e:
        return None
    
    return(df)
