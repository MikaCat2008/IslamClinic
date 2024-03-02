import flask as f

from . import tools as t

from . import api_routers
from . import main_routers
from . import patient_routers
from . import employee_routers
from . import session_routers


def add_routers(app: f.Flask) -> None:
    for url, method, handler in t.routers:
        app.route(url, methods=[method])(handler)
