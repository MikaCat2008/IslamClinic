from flask import Flask

from routers import tools, add_routers
from controller import Controller

from model import Model
from database import Database


class Application:
    def __init__(self, database_path: str) -> None:
        self.database = Database(database_path)
        Model.database = self.database

        self.controller = Controller()
        self.flask_application = Flask(__name__)

        tools.controller = self.controller

        add_routers(self.flask_application)

    def reset(self) -> None:
        self.database.reset()
        self.controller.reset_models()

    def run(self) -> None:
        self.flask_application.run(
            host = "localhost",
            port = 8080
        )
