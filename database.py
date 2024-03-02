import sqlite3


class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database/database.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

    def execute(self, query: str, *args) -> sqlite3.Cursor:
        cursor = self.cursor.execute(query, args)
        
        self.connection.commit()

        return cursor
        

database = Database()
