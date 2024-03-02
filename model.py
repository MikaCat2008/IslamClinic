from database import database, Database


class Model:
    database: Database

    def __init_subclass__(cls) -> None:
        cls.database = database
        
        return cls
