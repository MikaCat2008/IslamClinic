import flask as f

from . import tools as t


@t.route("/add-employee", auth=True)
def add_employee() -> f.Response:
    return f.render_template("employee/add_employee.html", texts=t.texts)


@t.route("/edit-employee", auth=True)
def edit_employee() -> f.Response:
    employee = t.controller.employee.get(t.arg("employeeId"))[0]
    
    return f.render_template(
        "employee/edit_employee.html", 
        employee=employee.get_data(),
        texts=t.texts
    )

@t.route("/employees", auth=True)
def employees() -> f.Response:
    return f.render_template("employee/employees.html", texts=t.texts)
