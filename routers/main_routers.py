import flask as f

from . import tools as t


@t.route("/login")
def login() -> f.Response:
    if t.is_authed():
        return f.redirect("/")

    return f.render_template("login.html")


@t.route("/", auth=True)
def index() -> f.Response:
    return f.render_template("index.html")
