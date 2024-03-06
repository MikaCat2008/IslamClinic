import flask as f

from . import tools as t


@t.route("/add-session", auth=True)
def add_session() -> f.Response:
    return f.render_template("session/add_session.html", texts=t.texts)


@t.route("/edit-session", auth=True)
def edit_session() -> f.Response:
    session = t.controller.session.get(t.arg("sessionId"))[0]
    
    return f.render_template(
        "session/edit_session.html", 
        session=session.get_data(),
        texts=t.texts
    )

@t.route("/schedules", auth=True)
def schedule() -> f.Response:
    return f.render_template("session/schedules.html", texts=t.texts)
