import sqlite3
import pandas as pd

class Players:
    """Players class to manage database connection and data retrieval."""
    path: str
    
    # Add an __init__ method to accept the 'path' argument
    def __init__(self, path: str):
        self.path = path
    
    def players_dataframe(self) -> pd.DataFrame:
        """
        Retrieve the Players table as a pandas DataFrame.
        
        Returns:
            pd.DataFrame: The Players table data
        """
        # Connect to the database
        con = sqlite3.connect(self.path)
        
        try:
            # Query the Players table
            query = "SELECT * FROM Players"
            results_df = pd.read_sql_query(query, con)
            
        finally:
            # Always close the connection
            con.close()
        
        return results_df


def get_Players_instance(db_path: str) -> Players:
    """
    Factory function to create a Players instance.
    
    Args:
        db_path: Path to the database file
        
    Returns:
        Players: A new Players instance
    """
    return Players(path=db_path)

