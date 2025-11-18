# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_21_DisplayDataframeWeb.py
# DATE 2025-10-25
# DESCRIPTION: 

import streamlit as st
import pandas as pd
import sqlite3
import os

# Set page config
st.set_page_config(page_title="Dataframe Display", layout="wide")

# Connect to database and fetch data
@st.cache_data
def load_data():
    path_to_database = os.path.join(os.getenv("EXAMPLES", ""), "Boxscores.db")
    # Alternate path: path_to_database = "Boxscores.db"
    
    con = sqlite3.connect(path_to_database)
    query = "SELECT * FROM Boxscores"
    df = pd.read_sql_query(query, con)
    con.close()
    
    return df

# Load data
results_df = load_data()

# Title
st.title("Dataframe Display")

# Sidebar
with st.sidebar:
    st.header("Data Information")
    st.text(f"Rows: {len(results_df)} | Columns: {len(results_df.columns)}")
    st.divider()
    st.write("Use the search box and column filters to explore the data.")

# Main panel
st.subheader("Data Table")

# Add search functionality
search_term = st.text_input("Search across all columns:", "")

# Filter dataframe based on search
if search_term:
    mask = results_df.astype(str).apply(
        lambda x: x.str.contains(search_term, case=False, na=False)
        ).any(axis=1)

    filtered_df = results_df[mask]
else:
    filtered_df = results_df

# Display dataframe with built-in sorting and filtering
st.dataframe(
    filtered_df,
    hide_index=True
)

# Display row count after filtering
st.caption(f"Showing {len(filtered_df)} of {len(results_df)} rows")

################################################################################
# To run this, in terminal type: streamlit run /absolute path to this program/ #
################################################################################