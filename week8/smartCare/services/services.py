from domain import Appointment
from repositories import AppointmentRepository


class AppointmentService:
    def __init__(self, repository: AppointmentRepository):
        self.repository = repository

    def book_appointment(self, patient_name: str, practitioner_name: str, appointment_time: str):
        if not patient_name or not patient_name.strip():
            raise ValueError("Patient name cannot be empty")

        appointment = Appointment(patient_name, practitioner_name, appointment_time)
        self.repository.save(appointment)

    def get_appointments(self):
        return self.repository.get_all()