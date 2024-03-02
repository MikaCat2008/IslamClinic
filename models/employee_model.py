from model import Model


class EmployeeModel(Model):
    def __init__(
        self, id: int, fullname: str, age: int, gender: bool, salary: int, job_category: int,
        job_title: int
    ) -> None:
        self.id = id
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.salary = salary
        self.job_category = job_category
        self.job_title = job_title

    def get_data(self) -> dict[str, object]:
        return {
            "id": self.id,
            "fullname": self.fullname,
            "age": self.age,
            "gender": self.gender,
            "salary": self.salary,
            "jobCategory": self.job_category,
            "jobTitle": self.job_title
        }

    @classmethod
    def init(cls) -> None:
        cls.database.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                fullname STRING,
                age INTEGER,
                gender BOOLEAN,
                salary INT,
                jobCategory INT,
                jobTitle INT
            );
        """)

    @classmethod
    def create(
        cls, fullname: str, age: int, gender: bool, salary: int, job_category: int,
        job_title: int
    ) -> 'EmployeeModel':
        cls.emit("onCreate", {
            "fullname": fullname, "age": age, "gender": gender, "salary": salary,
            "job_category": job_category, "job_title": job_title
        })

        id = cls.database.execute("""
            INSERT INTO employees VALUES(NULL, ?, ?, ?, ?, ?, ?);
        """, fullname, age, gender, salary, job_category, job_title).lastrowid

        return cls(id, fullname, age, gender, salary, job_category, job_title)
    
    @classmethod
    def get(
        cls, id: int = None, fullname: str = None, age: int = None, gender: bool = None, 
        salary: str = None, job_category: int = None, job_title: int = None
    ) -> None:
        cls.emit("onGet", {
            "id": id, "fullname": fullname, "age": age, "gender": gender, "salary": salary,
            "job_category": job_category, "job_title": job_title
        })
        
        c = list(filter(None.__ne__, (id, fullname, age, gender, salary, job_category, job_title)))

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
            if salary is not None:
                cs.append("salary = ?")
            if job_category is not None:
                cs.append("jobCategory = ?")
            if job_title is not None:
                cs.append("jobTitle = ?")

            where = " WHERE " + " AND ".join(cs)

        return list(map(
            lambda a: cls(*a),
            cls.database.execute(f"""
                SELECT * FROM employees{where} LIMIT 100;
            """, *c).fetchall()
        ))

    @classmethod
    def edit(
        cls, id: int, fullname: str, age: int, gender: bool, salary: int, job_category: int,
        job_title: int
    ) -> None:
        cls.emit("onEdit", {
            "id": id, "fullname": fullname, "age": age, "gender": gender, "salary": salary,
            "job_category": job_category, "job_title": job_title
        })

        cls.database.execute("""
            UPDATE employees 
            SET fullname = ?,
                age = ?,
                gender = ?,
                salary = ?,
                jobCategory = ?,
                jobTitle = ?
            WHERE id = ?;
        """, fullname, age, gender, salary, job_category, job_title, id)

        return cls(id, fullname, age, gender, salary, job_category, job_title)

    @classmethod
    def delete(cls, id: int) -> None:
        cls.emit("onDelete", {
            "id": id
        })
        
        cls.database.execute("""
            DELETE FROM employees WHERE id = ?; 
        """, id)
