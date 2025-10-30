import pandas as pd
import sqlite3

class Teams:
    """Teams class for accessing Teams database"""
    path: str
    
    def __init__(self, path_to_database: str = ""):
        """
        Initialize Teams object with database path
        
        Args:
            path_to_database: Path to the SQLite database file
        """
        self.path = path_to_database
    
    def teams_dataframe(self) -> pd.DataFrame:
        """
        Retrieve Teams data from database as a pandas DataFrame
        
        Returns:
            DataFrame containing Teams table data
        """
        # Connect to database
        con = sqlite3.connect(self.path)
        
        try:
            # Query the Teams table
            query = "SELECT * FROM Teams"
            results_df = pd.read_sql_query(query, con)
            
            return results_df
        
        finally:
            # Always close the connection
            con.close()


def get_Teams_instance(db_path: str) -> Teams:
    """
    Factory function to create a Teams instance
    
    Args:
        db_path: Path to the database
        
    Returns:
        Teams object
    """
    return Teams(path_to_database=db_path)

