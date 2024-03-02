from flask import Flask

from controller import Controller
from routers import tools, add_routers


class Application:
    def __init__(self) -> None:
        self.controller = Controller()
        self.flask_application = Flask(__name__)

        tools.controller = self.controller

        add_routers(self.flask_application)

    def run(self) -> None:
        self.flask_application.run(
            host = "localhost",
            port = 8080
        )
