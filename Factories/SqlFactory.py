import pyodbc 
from dotenv import load_dotenv
import os


class SqlFactory:
    '''Class for SQL Factory'''

    load_dotenv()

    def __init__(self):
        self.conn = pyodbc.connect(os.environ["SQL_SERVER"])
        self.cursor = self.conn.cursor()
    
    def query_sql(self, query):
        return self.cursor.execute(query).fetchall()
    
    def query_columns(self, db, columns):
        
        query = f"SELECT {columns} FROM {db}"
        return self.query_sql(query)