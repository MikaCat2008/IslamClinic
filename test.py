import unittest

from models import PatientModel, EmployeeModel, SessionModel

from application import Application

patients = [
    ("Романенко Кристина Романовна", 25, False, "Юдина Елена Романовна"),
    ("Устинов Николай Ярославович", 27, True, "Юдина Елена Романовна")
]
employees = [
    ("Юдина Елена Романовна", 34, False, 1200, 0, 0),
    ("Щукин Игнат Эдуардович", 36, True, 1300, 0, 0)
]
sessions = [
    ("Романенко Кристина Романовна", "Юдина Елена Романовна", 1709373600),
    ("Устинов Николай Ярославович", "Юдина Елена Романовна", 1709377200)
]


def create_patients() -> list[PatientModel]:
    return [
        patient.create(*patients[0]),
        patient.create(*patients[1])
    ]


def delete_patients() -> None:
    patient.delete(1)
    patient.delete(2)


def create_employees() -> list[EmployeeModel]:
    return [
        employee.create(*employees[0]),
        employee.create(*employees[1])
    ]


def delete_employees() -> None:
    employee.delete(1)
    employee.delete(2)


def create_sessions() -> list[SessionModel]:
    return [
        session.create(*sessions[0]),
        session.create(*sessions[1])
    ]


def delete_sessions() -> None:
    session.delete(1)
    session.delete(2)


class PatientCase(unittest.TestCase):
    def test_create_patient(self) -> None:
        patient1, patient2 = create_patients()

        self.assertEqual(patient1, PatientModel(1, *patients[0]))
        self.assertEqual(patient2, PatientModel(2, *patients[1]))

        delete_patients()

    def test_get_patients(self) -> None:
        create_patients()
        
        _patients = patient.get()

        self.assertEqual(_patients, [
            PatientModel(1, *patients[0]),
            PatientModel(2, *patients[1])
        ])

        delete_patients()

    def test_edit_patient(self) -> None:
        patient1, patient2 = create_patients()

        patient.edit(
            patient1.id, patient2.fullname, patient2.age, patient2.gender, 
            patient2.family_doctor_fullname
        )
        patient.edit(
            patient2.id, patient1.fullname, patient1.age, patient1.gender, 
            patient1.family_doctor_fullname
        )

        _patients = patient.get()

        self.assertEqual(_patients[0], PatientModel(1, *patients[1]))
        self.assertEqual(_patients[1], PatientModel(2, *patients[0]))

        delete_patients()

    def test_delete_patient(self) -> None:
        create_patients()
        delete_patients()

        _patients = patient.get()

        self.assertEqual(_patients, [])


class EmployeeCase(unittest.TestCase):
    def test_create_employee(self) -> None:
        employee1, employee2 = create_employees()

        self.assertEqual(employee1, EmployeeModel(1, *employees[0]))
        self.assertEqual(employee2, EmployeeModel(2, *employees[1]))

        delete_employees()

    def test_get_employees(self) -> None:
        create_employees()
        
        _employees = employee.get()

        self.assertEqual(_employees, [
            EmployeeModel(1, *employees[0]),
            EmployeeModel(2, *employees[1])
        ])

        delete_employees()

    def test_edit_employee(self) -> None:
        employee1, employee2 = create_employees()

        employee.edit(
            employee1.id, employee2.fullname, employee2.age, employee2.gender, 
            employee2.salary, employee2.job_category, employee2.job_title
        )
        employee.edit(
            employee2.id, employee1.fullname, employee1.age, employee1.gender, 
            employee1.salary, employee1.job_category, employee1.job_title
        )

        _employees = employee.get()

        self.assertEqual(_employees[0], EmployeeModel(1, *employees[1]))
        self.assertEqual(_employees[1], EmployeeModel(2, *employees[0]))

        delete_employees()

    def test_delete_employee(self) -> None:
        create_employees()
        delete_employees()

        _employees = employee.get()

        self.assertEqual(_employees, [])


class SessionCase(unittest.TestCase):
    def test_create_session(self) -> None:
        session1, session2 = create_sessions()

        self.assertEqual(session1, SessionModel(1, *sessions[0]))
        self.assertEqual(session2, SessionModel(2, *sessions[1]))

        delete_sessions()

    def test_get_sessions(self) -> None:
        create_sessions()
        
        _sessions = session.get()

        self.assertEqual(_sessions, [
            SessionModel(1, *sessions[0]),
            SessionModel(2, *sessions[1])
        ])

        delete_sessions()

    def test_edit_session(self) -> None:
        session1, session2 = create_sessions()

        session.edit(
            session1.id, session2.patient_fullname, session2.employee_fullname, 
            session2.datetime_timestamp
        )
        session.edit(
            session2.id, session1.patient_fullname, session1.employee_fullname, 
            session1.datetime_timestamp
        )

        _sessions = session.get()

        self.assertEqual(_sessions[0], SessionModel(1, *sessions[1]))
        self.assertEqual(_sessions[1], SessionModel(2, *sessions[0]))

        delete_sessions()

    def test_delete_session(self) -> None:
        create_sessions()
        delete_sessions()

        _sessions = session.get()

        self.assertEqual(_sessions, [])


if __name__ == "__main__":
    application = Application("database/test_database.db")
    application.reset()

    controller = application.controller

    patient = controller.patient
    employee = controller.employee
    session = controller.session

    unittest.main()
