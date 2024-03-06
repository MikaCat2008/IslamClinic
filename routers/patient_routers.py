import flask as f

from . import tools as t


@t.route("/add-patient", auth=True)
def add_patient() -> f.Response:
    return f.render_template("patient/add_patient.html", texts=t.texts)


@t.route("/edit-patient", auth=True)
def edit_patient() -> f.Response:
    patient = t.controller.patient.get(t.arg("patientId"))[0]
    
    return f.render_template(
        "patient/edit_patient.html", 
        patient=patient.get_data(),
        texts=t.texts
    )

@t.route("/patients", auth=True)
def patients() -> f.Response:
    return f.render_template("patient/patients.html", texts=t.texts)
