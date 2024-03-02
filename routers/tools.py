import typing as t
from functools import wraps

import flask as f

LOGIN_USERNAME = "Admin"
LOGIN_PASSWORD = "Root"

REDIRECT_URL = "/login"

routers: list[tuple[str, str, t.Callable]] = []
controller = None


def is_authed() -> bool:
    cookies = f.request.cookies
        
    username = cookies.get("username")
    password = cookies.get("password")

    return True

    return username == LOGIN_USERNAME and password == LOGIN_PASSWORD


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
