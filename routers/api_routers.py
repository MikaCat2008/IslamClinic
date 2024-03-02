import time, datetime as dt, collections as c, flask as f

from . import tools as t


def create_patient(data: dict[str, object]) -> dict[str, object]:
    fullname = data["fullname"]
    age = int(data["age"])
    gender = bool(int(data["gender"]))
    family_doctor_fullname = data["familyDoctorFullname"]

    t.controller.patient.create(fullname, age, gender, family_doctor_fullname)

    return {}


def get_patients(data: dict[str, object]) -> dict[str, object]:
    id = data["id"]
    fullname = data["fullname"]
    age = data["age"]
    gender = data["gender"]
    family_doctor_fullname = data["familyDoctorFullname"]

    if id == "": id = None
    else: id = int(id)

    if fullname == "": fullname = None

    if age == "": age = None
    else: age = int(age)

    if gender == "": gender = None
    else: gender = bool(int(gender))

    if family_doctor_fullname == "": family_doctor_fullname = None

    patients = t.controller.patient.get(id, fullname, age, gender, family_doctor_fullname)

    return {
        "patients": [patient.get_data() for patient in patients]
    }


def edit_patient(data: dict[str, object]) -> dict[str, object]:
    id = data["id"]
    fullname = data["fullname"]
    age = int(data["age"])
    gender = bool(int(data["gender"]))
    family_doctor_fullname = data["familyDoctorFullname"]

    t.controller.patient.edit(id, fullname, age, gender, family_doctor_fullname)

    return {}


def delete_patient(data: dict[str, object]) -> dict[str, object]:
    id = int(data["id"])

    t.controller.patient.delete(id)

    return {}


def create_employee(data: dict[str, object]) -> dict[str, object]:
    fullname = data["fullname"]
    age = int(data["age"])
    gender = bool(int(data["gender"]))
    salary = int(data["salary"])
    job_category = int(data["jobCategory"])
    job_title = int(data["jobTitle"])

    t.controller.employee.create(fullname, age, gender, salary, job_category, job_title)

    return {}


def get_employees(data: dict[str, object]) -> dict[str, object]:
    id = data["id"]
    fullname = data["fullname"]
    age = data["age"]
    gender = data["gender"]
    salary = data["salary"]
    job_category = data["jobCategory"]
    job_title = data["jobTitle"]

    if id == "": id = None
    else: id = int(id)

    if fullname == "": fullname = None

    if age == "": age = None
    else: age = int(age)

    if gender == "": gender = None
    else: gender = bool(int(gender))

    if salary == "": salary = None
    else: salary = int(salary)

    if job_category == "": job_category = None
    else: job_category = int(job_category)

    if job_title == "": job_title = None
    else: job_title = int(job_title)

    employees = t.controller.employee.get(id, fullname, age, gender, salary, job_category, job_title)

    return {
        "employees": [employee.get_data() for employee in employees]
    }


def edit_employee(data: dict[str, object]) -> dict[str, object]:
    id = int(data["id"])
    fullname = data["fullname"]
    age = int(data["age"])
    gender = bool(int(data["gender"]))
    salary = int(data["salary"])
    job_category = int(data["jobCategory"])
    job_title = int(data["jobTitle"])

    t.controller.employee.edit(id, fullname, age, gender, salary, job_category, job_title)

    return {}


def delete_employee(data: dict[str, object]) -> dict[str, object]:
    id = int(data["id"])

    t.controller.employee.delete(id)

    return {}


def create_session(data: dict[str, object]) -> dict[str, object]:
    patient_fullname = data["patientFullname"]
    employee_fullname = data["employeeFullname"]
    datetime_timestamp = int(data["datetimeTimestamp"])

    t.controller.session.create(patient_fullname, employee_fullname, datetime_timestamp)
    
    return {}


def edit_session(data: dict[str, object]) -> dict[str, object]:
    id = int(data["id"])
    patient_fullname = data["patientFullname"]
    employee_fullname = data["employeeFullname"]
    datetime_timestamp = int(data["datetimeTimestamp"])

    t.controller.session.edit(id, patient_fullname, employee_fullname, datetime_timestamp)
    
    return {}


def delete_session(data: dict[str, object]) -> dict[str, object]:
    id = int(data["id"])

    t.controller.session.delete(id)
    
    return {}


def get_schedules(data: dict[str, object]) -> dict[str, object]:
    patient_fullname = data["patientFullname"]
    employee_fullname = data["employeeFullname"]
    datetime_timestamp = data["datetimeTimestamp"]

    if patient_fullname == "": patient_fullname = None

    if employee_fullname == "": employee_fullname = None

    datetime_timestamp = int(datetime_timestamp)

    sessions = t.controller.session.get(None, patient_fullname, employee_fullname, datetime_timestamp)

    _schedules = c.defaultdict(list)

    for session in sessions:
        _schedules[session.employee_fullname].append({
            "id": session.id,
            "time": f"{dt.datetime.fromtimestamp(session.datetime_timestamp):%H:%M}",
            "patientFullname": session.patient_fullname
        })

    schedules = []

    for employee_fullname, _sessions in _schedules.items():        
        schedules.append({
            "employeeFullname": employee_fullname,
            "sessions": _sessions
        })
    
    return {
        "schedules": schedules
    }


@t.route("/api", method="POST", auth=True)
def api() -> f.Response:
    json = f.request.json
    
    method = json["method"]
    data = json["data"]

    print(method, data)

    match method:
        case "createPatient":
            response = create_patient(data)
        case "getPatients":
            response = get_patients(data)
        case "editPatient":
            response = edit_patient(data)
        case "deletePatient":
            response = delete_patient(data)

        case "createEmployee":
            response = create_employee(data)
        case "getEmployees":
            response = get_employees(data)
        case "editEmployee":
            response = edit_employee(data)
        case "deleteEmployee":
            response = delete_employee(data)

        case "createSession":
            response = create_session(data)
        case "editSession":
            response = edit_session(data)
        case "deleteSession":
            response = delete_session(data)
        case "getSchedules":
            response = get_schedules(data)

    return f.jsonify(response)
 