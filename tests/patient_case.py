import unittest as u

from models.patient_model import PatientModel
from application import Application

patient: PatientModel = None
application: Application = None

patients = [
    ("Романенко Кристина Романовна", 25, False, "Юдина Елена Романовна"),
    ("Устинов Николай Ярославович", 27, True, "Юдина Елена Романовна")
]


def create_patients() -> list[tuple[int, int, float]]:
    return [
        patient.create(*patients[0]),
        patient.create(*patients[1])
    ]


def delete_patients() -> None:
    patient.delete(1)
    patient.delete(2)


class PatientCase(u.TestCase):
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
