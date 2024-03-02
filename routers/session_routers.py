import flask as f

from . import tools as t

session = {
    "get_data": lambda: {
        "id": 1,
        "patientFullname": "Лукашенко Игорь Борисович",
        "employeeFullname": "Путин Виктор Ильич",
        "sessionDatetime": 1709237875
    }
}


@t.route("/add-session", auth=True)
def add_session() -> f.Response:
    return f.render_template("session/add_session.html")


@t.route("/edit-session", auth=True)
def edit_session() -> f.Response:
    session = t.controller.session.get(t.arg("sessionId"))[0]
    
    return f.render_template(
        "session/edit_session.html", 
        session=session.get_data()
    )

@t.route("/schedule", auth=True)
def schedule() -> f.Response:
    return f.render_template("session/schedule.html")
