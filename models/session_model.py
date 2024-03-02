from model import Model


class SessionModel(Model):
    def __init__(
        self, id: int, patient_fullname: str, employee_fullname: str, datetime_timestamp: int
    ) -> None:
        self.id = id
        self.patient_fullname = patient_fullname
        self.employee_fullname = employee_fullname
        self.datetime_timestamp = datetime_timestamp

    def get_data(self) -> dict[str, object]:
        return {
            "id": self.id,
            "patientFullname": self.patient_fullname,
            "employeeFullname": self.employee_fullname,
            "datetimeTimestamp": self.datetime_timestamp
        }

    @classmethod
    def init(cls) -> None:
        cls.database.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY,
                patientFullname STRING,
                employeeFullname STRING,
                datetimeTimestamp INTEGER
            );
        """)

    @classmethod
    def create(
        cls, patient_fullname: str, employee_fullname: str, datetime_timestamp: int
    ) -> None:
        return cls.database.execute("""
            INSERT INTO sessions VALUES(NULL, ?, ?, ?);
        """, patient_fullname, employee_fullname, datetime_timestamp)
    
    @classmethod
    def get(
        cls, id: int = None, patient_fullname: str = None, employee_fullname: int = None, 
        datetime_timestamp: bool = None
    ) -> None:
        c = list(filter(None.__ne__, (id, patient_fullname, employee_fullname, datetime_timestamp)))

        where = ""
        if c:
            cs = []

            if id is not None:
                cs.append("id = ?")
            if patient_fullname is not None:
                cs.append("patientFullname = ?")
            if employee_fullname is not None:
                cs.append("employeeFullname = ?")
            if datetime_timestamp is not None:
                cs.append("datetimeTimestamp - ? BETWEEN 0 AND 86400")

            where = " WHERE " + " AND ".join(cs)

        return list(map(
            lambda a: cls(*a),
            cls.database.execute(f"""
                SELECT * FROM sessions{where} LIMIT 100;
            """, *c).fetchall()
        ))

    @classmethod
    def edit(
        cls, id: int, patient_fullname: str, employee_fullname: str, datetime_timestamp: int
    ) -> None:
        cls.database.execute("""
            UPDATE sessions 
            SET patientFullname = ?,
                employeeFullname = ?,
                datetimeTimestamp = ?
            WHERE id = ?;
        """, patient_fullname, employee_fullname, datetime_timestamp, id)

    @classmethod
    def delete(cls, id: int) -> None:
        cls.database.execute("""
            DELETE FROM sessions WHERE id = ?; 
        """, id)
