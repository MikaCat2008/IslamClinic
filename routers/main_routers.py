import flask as f

from . import tools as t


@t.route("/login")
def login() -> f.Response:
    if t.is_authed():
        return f.redirect("/")

    return f.render_template("login.html", texts=t.texts)


@t.route("/", auth=True)
def index() -> f.Response:
    return f.render_template("index.html", texts=t.texts)


@t.route("/_login", method="POST", auth=False)
def _login() -> f.Response:
    json = f.request.json
        
    username = json.get("username")
    password = json.get("password")

    status = t.check_data(username, password)

    response = f.jsonify({"status": status})

    if status:
        response.set_cookie("username", username)
        response.set_cookie("password", password)
    
    return response


@t.route("/exit", method="GET", auth=True)
def exit() -> f.Response:
    response = f.redirect("/")

    response.delete_cookie("username")
    response.delete_cookie("password")
    
    return response

@t.route("/texts.js", method="GET", auth=False)
def texts() -> f.Response:
    return f"let texts = { t.texts };"
