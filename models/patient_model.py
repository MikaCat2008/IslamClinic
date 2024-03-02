from model import Model


class PatientModel(Model):
    def __init__(
        self, id: int, fullname: str, age: int, gender: bool, family_doctor_fullname: str
    ) -> None:
        self.id = id
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.family_doctor_fullname = family_doctor_fullname

    def get_data(self) -> dict[str, object]:
        return {
            "id": self.id,
            "fullname": self.fullname,
            "age": self.age,
            "gender": self.gender,
            "familyDoctorFullname": self.family_doctor_fullname
        }

    @classmethod
    def init(cls) -> None:
        cls.database.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                fullname STRING,
                age INTEGER,
                gender BOOLEAN,
                familyDoctorFullname STRING
            );
        """)

    @classmethod
    def create(
        cls, fullname: str, age: int, gender: bool, family_doctor_fullname: str
    ) -> 'PatientModel':
        cls.emit("onCreate", {
            "fullname": fullname, "age": age, "gender": gender, 
            "family_doctor_fullname": family_doctor_fullname
        })

        id = cls.database.execute("""
            INSERT INTO patients VALUES(NULL, ?, ?, ?, ?);
        """, fullname, age, gender, family_doctor_fullname).lastrowid

        return cls(id, fullname, age, gender, family_doctor_fullname)
    
    @classmethod
    def get(
        cls, id: int = None, fullname: str = None, age: int = None, gender: bool = None, 
        family_doctor_fullname: str = None
    ) -> list['PatientModel']:
        cls.emit("onGet", {
            "id": id, "fullname": fullname, "age": age, "gender": gender,
            "family_doctor_fullname": family_doctor_fullname
        })

        c = list(filter(None.__ne__, (id, fullname, age, gender, family_doctor_fullname)))

        where = ""
        if c:
            cs = []

            if id is not None:
                cs.append("id = ?")
            if fullname is not None:
                cs.append("fullname = ?")
            if age is not None:
                cs.append("age = ?")
            if gender is not None:
                cs.append("gender = ?")
            if family_doctor_fullname is not None:
                cs.append("familyDoctorFullname = ?")

            where = " WHERE " + " AND ".join(cs)

        return list(map(
            lambda a: cls(*a),
            cls.database.execute(f"""
                SELECT * FROM patients{where} LIMIT 100;
            """, *c).fetchall()
        ))

    @classmethod
    def edit(
        cls, id: int, fullname: str, age: int, gender: bool, family_doctor_fullname: str
    ) -> 'PatientModel':
        cls.emit("onEdit", {
            "id": id, "fullname": fullname, "age": age, "gender": gender, 
            "family_doctor_fullname": family_doctor_fullname
        })

        cls.database.execute("""
            UPDATE patients 
            SET fullname = ?,
                age = ?,
                gender = ?,
                familyDoctorFullname = ?
            WHERE id = ?;
        """, fullname, age, gender, family_doctor_fullname, id)

        return cls(id, fullname, age, gender, family_doctor_fullname)

    @classmethod
    def delete(cls, id: int) -> None:
        cls.emit("onDelete", {
            "id": id
        })
        
        cls.database.execute("""
            DELETE FROM patients WHERE id = ?; 
        """, id)
