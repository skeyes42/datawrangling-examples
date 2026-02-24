import os
import sys
import pandas as pd
from pyRserve import connect
from pyRserve.taggedContainers import TaggedList

def get_boxscores_via_rserve():
    """
    Connect to Rserve and retrieve enriched Boxscores data.
    Returns a pandas DataFrame.
    """

    # --- Resolve paths ---
    examples_dir = os.getenv("EXAMPLES")
    if not examples_dir:
        raise ValueError("EXAMPLES environment variable not set")

    db_path = os.path.join(examples_dir, "Boxscores.db")
    r_class_path = os.path.join(examples_dir, "LIBRARY", "BoxscoresClass.R")
    r_class_path = r_class_path.replace("\\", "/")

    # --- Connect to Rserve ---
    print("Connecting to Rserve...")
    try:
        conn = connect(host="localhost", port=6311)
        print("Connected successfully")
    except ConnectionRefusedError:
        print("Error: Could not connect to Rserve")
        print("Make sure Rserve is running:")
        print("  library(Rserve)")
        print("  Rserve(args='--no-save')")
        return None

    try:
        # Send DB path into R
        conn.r.db_path = db_path

        # Load R class
        print(f"Loading R class from {r_class_path}")
        conn.eval(f'source("{r_class_path}")')

        # Call R function
        print("Retrieving Boxscores data...")
        result_df = conn.eval("get_Boxscores_data()")

        print(f"Retrieved {len(result_df)} rows")

        # --- Convert R result to pandas DataFrame ---
        # TaggedList has 'keys' and 'values' attributes
        data = {}
        for i in range(len(result_df.keys)):
            col_name = result_df.keys[i]
            col_data = result_df.values[i]
            data[col_name] = col_data
        
        df = pd.DataFrame(data)

        print("Conversion successful")
        return df

    finally:
        conn.close()
        print("Connection closed")

def main():
    """Main function to demonstrate Rserve with Boxscores database"""

    print(sys.executable)

    df = get_boxscores_via_rserve()

    if df is None:
        print("Failed to retrieve data")
        return

    # --- DataFrame summary ---
    print("\n--- DataFrame Info ---")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

    print("\n--- First Few Rows ---")
    print(df.head())

    print("\n--- Summary Statistics ---")
    numeric_cols = ["FGM", "FG3M", "FTM"]
    print(df[numeric_cols].describe())

    # Example: filter high scorers
    high_scorers = df[df["FGM"] > 8]
    print("\n--- High Scoring Performances (FGM > 8) ---")
    print(high_scorers[["GAME_ID", "PLAYER_NAME", "TEAM_NAME", "FGM"]])

    print("\nDone")


if __name__ == "__main__":
    main()