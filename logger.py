import logging

from datetime import date

log = logging.getLogger('werkzeug')
log.disabled = True


class Logger:
    def run_application(self) -> None:
        logging.info("Сервер запущен")

    def stop_application(self) -> None:
        logging.info("Сервер остановлен")

    def create_patient(
        self, fullname: str, age: int, gender: bool, family_doctor_fullname: str
    ) -> None:
        args = "(fullname={}, age={}, gender={}, family_doctor_fullname={})".format(
            fullname, age, gender, family_doctor_fullname
        )

        logging.info(f"Добавлен пациент{args}")

    def get_patients(
        self, id: int, fullname: str, age: int, gender: bool, family_doctor_fullname: str
    ) -> None:
        args = "(id={}, fullname={}, age={}, gender={}, family_doctor_fullname={})".format(
            id, fullname, age, gender, family_doctor_fullname
        )

        logging.info(f"Запрос на список пациентов{args}")

    def edit_patient(
        self, id: int, fullname: str, age: int, gender: bool, family_doctor_fullname: str
    ) -> None:
        args = "(id={}, fullname={}, age={}, gender={}, family_doctor_fullname={})".format(
            id, fullname, age, gender, family_doctor_fullname
        )

        logging.info(f"Изменена информация о пациенте{args}")
    
    def delete_patient(self, id: int) -> None:
        logging.info(f"Пациент под номером {id} удален")

    def create_employee(
        self, fullname: str, age: int, gender: bool, salary: int, job_category: int, job_title: int
    ) -> None:
        args = "(fullname={}, age={}, gender={}, family_doctor_fullname={})".format(
            fullname, age, gender, salary, job_category, job_title
        )

        logging.info(f"Добавлен сотрудник{args}")

    def get_employees(
        self, id: int, fullname: str, age: int, gender: bool, salary: int,
        job_category: int, job_title: int
    ) -> None:
        args = "(id={}, fullname={}, age={}, gender={}, salary={}, job_category={}, job_title={})".format(
            id, fullname, age, gender, salary, job_category, job_title
        )

        logging.info(f"Запрос на список сотрудников{args}")

    def edit_employee(
        self, id: int, fullname: str, age: int, gender: bool, salary: int, job_category: int, 
        job_title: int
    ) -> None:
        args = "(id={}, fullname={}, age={}, gender={}, salary={}, job_category={}, job_title={})".format(
            id, fullname, age, gender, salary, job_category, job_title
        )

        logging.info(f"Изменена информация о сотруднике{args}")
    
    def delete_employee(self, id: int) -> None:
        logging.info(f"Сотрудник под номером {id} удален")

    def create_session(
        self, patient_fullname: str, employee_fullname: str, datetime_timestamp: int
    ) -> None:
        args = "(patient_fullname={}, employee_fullname={}, datetime_timestamp={})".format(
            patient_fullname, employee_fullname, datetime_timestamp
        )

        logging.info(f"Назначен сеанс{args}")

    def get_sessions(
        self, id: int, patient_fullname: str, employee_fullname: str, datetime_timestamp: int
    ) -> None:
        args = "(id={}, patient_fullname={}, employee_fullname={}, datetime_timestamp={})".format(
            id, patient_fullname, employee_fullname, datetime_timestamp
        )

        logging.info(f"Запрос на список сеансов{args}")

    def edit_session(
        self, id: int, patient_fullname: str, employee_fullname: str, datetime_timestamp: int
    ) -> None:
        args = "(id={}, patient_fullname={}, employee_fullname={}, datetime_timestamp={})".format(
            id, patient_fullname, employee_fullname, datetime_timestamp
        )

        logging.info(f"Изменена информация о сеансе{args}")
    
    def delete_session(self, id: int) -> None:
        logging.info(f"Сеанс под номером {id} удален")


logger = Logger()
logging.basicConfig(
    level=logging.INFO, 
    filename="hotel.log", filemode="w", encoding="UTF-8",
    format="%(asctime)s: %(message)s"
)
