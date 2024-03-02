import os, sqlite3


class Database:
    def __init__(self, database_path: str) -> None:
        self.database_path = database_path
        self.connection = sqlite3.connect(database_path, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def reset(self) -> None:
        self.connection.close()

        os.remove(self.database_path)
        
        self.__init__(self.database_path)

    def execute(self, query: str, *args) -> sqlite3.Cursor:
        cursor = self.cursor.execute(query, args)
        
        self.connection.commit()

        return cursor
