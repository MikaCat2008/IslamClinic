from models import PatientModel, EmployeeModel, SessionModel

from logger import logger


class Controller:
    def __init__(self) -> None:        
        self.patient = PatientModel        
        self.employee = EmployeeModel
        self.session = SessionModel

        self.init_models()

    def init_models(self) -> None:
        self.patient.init()

        self.patient.add_listener("onCreate", logger.create_patient)
        self.patient.add_listener("onGet", logger.get_patients)
        self.patient.add_listener("onEdit", logger.edit_patient)
        self.patient.add_listener("onDelete", logger.delete_patient)
        
        self.employee.init()

        self.employee.add_listener("onCreate", logger.create_employee)
        self.employee.add_listener("onGet", logger.get_employees)
        self.employee.add_listener("onEdit", logger.edit_employee)
        self.employee.add_listener("onDelete", logger.delete_employee)

        self.session.init()

        self.session.add_listener("onCreate", logger.create_session)
        self.session.add_listener("onGet", logger.get_sessions)
        self.session.add_listener("onEdit", logger.edit_session)
        self.session.add_listener("onDelete", logger.delete_session)

    def reset_models(self) -> None:
        self.patient.reset()
        self.employee.reset()
        self.session.reset()

        self.init_models()
