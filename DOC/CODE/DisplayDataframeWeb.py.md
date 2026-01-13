## DisplayDataframeWeb.py

This Python program is a **web application** built with Streamlit, designed to create an interactive dashboard for exploring data from a SQLite database.

**1. Core Infrastructure & Configuration**

**st.set_page_config(layout="wide")**: This sets the application to use the full width of your browser screen rather than a narrow centered column, which is ideal for large tables.

**Efficient Data Loading**: The @st.cache_data decorator ensures the database is only queried **once**. On subsequent page refreshes, the app retrieves the data from memory (cache) instead of hitting the database again, making the app much faster.

**2. Database Connection**

The load_data() function connects to Boxscores.db using the standard sqlite3 library.

It reads the entire Boxscores table into a **Pandas DataFrame** and then closes the connection to keep the system clean.

**3. Sidebar & User Interface**

**Sidebar Metrics**: The sidebar displays helpful "Data Information," such as the total number of rows and columns, giving the user an immediate sense of the dataset size.

**Search Box**: Users can type any text into the st.text_input field. The program instantly creates a "mask" that filters the rows to only show those where the search term appears in *any* column (names, teams, scores, etc.).

**4. Interactive Data Display**

**st.dataframe()**: This creates an interactive table on the main page.

**Built-in Tools**: In 2026, these interactive tables allow users to manually **sort columns**, **resize headers**, and **search specific values** directly within the table UI without additional code.

**Dynamic Captions**: A final note at the bottom updates in real-time to show how many rows are currently visible (e.g., "Showing 10 of 500 rows") after your filters are applied.

**Summary**

This is a professional-grade "internal tool" boilerplate. It allows a non-technical user to browse, search, and sort a basketball statistics database through a clean web interface rather than writing raw SQL queries.
