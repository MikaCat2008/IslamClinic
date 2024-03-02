from models import PatientModel, EmployeeModel, SessionModel


class Controller:
    def __init__(self) -> None:
        self.patient = PatientModel
        self.employee = EmployeeModel
        self.session = SessionModel

        self.patient.init()
        self.employee.init()
        self.session.init()
