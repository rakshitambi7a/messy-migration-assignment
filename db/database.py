import sqlite3
import threading
from contextlib import contextmanager
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Database:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, db_path=None):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, db_path=None):
        if not hasattr(self, 'initialized'):
            # Use the database path from the .env file or default to 'users.db'
            # Check multiple possible environment variable names
            self.db_path = (db_path or 
                           os.getenv('DATABASE_PATH') or 
                           os.getenv('DB_PATH') or 
                           'users.db')
            self.initialized = True
    
    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row  # Enable dict-like access
        try:
            yield conn
        finally:
            conn.close()
    
    def execute_query(self, query, params=None):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            return cursor.fetchall()
    
    def execute_one(self, query, params=None):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchone()