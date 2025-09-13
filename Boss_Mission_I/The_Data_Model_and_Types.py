
import sqlite3

class EventRepository:
    def __init__(self, db_path="events.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_table(self):       
        sql_command = """
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT
            )
        """
        self.cursor.execute(sql_command)
        self.conn.commit()





        
