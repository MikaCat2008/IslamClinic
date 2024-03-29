import typing as t
from functools import wraps

import flask as f

from texts import texts

LOGIN_USERNAME = "Admin"
LOGIN_PASSWORD = "Root"

REDIRECT_URL = "/login"

routers: list[tuple[str, str, t.Callable]] = []
controller = None


def check_data(username: str, password: str) -> bool:
    return username == LOGIN_USERNAME and password == LOGIN_PASSWORD


def is_authed() -> bool:
    cookies = f.request.cookies
        
    username = cookies.get("username")
    password = cookies.get("password")

    return check_data(username, password)


def route(url: str, method: str = "GET", auth: bool = False) -> t.Callable:
    def inner1(function: t.Callable) -> t.Callable:        
        @wraps(function)
        def inner2(*args, **kwargs) -> f.Response:
            if auth and not is_authed():
                return f.redirect(REDIRECT_URL)
            
            return function(*args, **kwargs)

        routers.append((url, method, inner2))

        return inner2

    return inner1

def arg(arg_name: str) -> object:
    return f.request.args.get(arg_name)
