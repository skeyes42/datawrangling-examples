## BoxscoresTKinter.py

This program creates a **Python desktop application** that displays sports-related data (Boxscores, Players, and Teams) in three side-by-side interactive lists. It is designed to act as a viewer for data stored in a SQLite database.

**1. Data Integration (The Backend)**

Before the window opens, the program sets up its data sources:

**Dynamic Paths**: It uses os.getenv("EXAMPLES") to find the database location on your system.

**Custom Modules**: It imports three specialized classes—BoxscoresClass, PlayersClass, and TeamsClass. These classes (likely defined in other files) handle the logic of connecting to the database and converting tables into **Pandas DataFrames**.

**Data Retrieval**: It creates three DataFrames: one for game boxscores, one for players, and one for teams.

**2. The User Interface (The Frontend)**

The TripleListboxApp class builds the GUI using tkinter:

**Triple Layout**: The window is split into three labeled sections: "DataFrame 1" (Boxscores), "DataFrame 2" (Players), and "DataFrame 3" (Teams).

**Listboxes and Scrollbars**: Each section contains a Listbox for viewing rows of data and a Scrollbar for navigating large datasets.

**Data Formatting**:

**Boxscores**: Displays a simplified "Game ID" for each entry.

**Players & Teams**: Concatenates all column data into a single string (e.g., Name: John Doe \| Team: Lakers) so you can see multiple details in one line.

**3. Interactivity**

The program is "event-driven," meaning it reacts to your actions:

**Selection Events**: When you click an item in any of the three lists, the program triggers a "selection event" (on_select_listbox).

**Console Feedback**: When an item is selected, the program looks up the full, original record from the DataFrame using iloc and prints the complete details to your terminal or console.

**Summary of Workflow (2026)**

**Initialize**: Loads data from Boxscores.db via external Python modules.

**Render**: Opens an 800x500 window and populates the lists with formatted data.

**Interact**: Allows you to scroll through and click records to see their full technical details in the background console.

This structure is a classic example of a **Model-View-Controller (MVC)** pattern, where the DataFrames are the "Model," the Tkinter window is the "View," and the selection functions act as the "Controller."
