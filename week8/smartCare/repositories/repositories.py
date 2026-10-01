from persistence import DATABASE
from domain import Appointment

class AppointmentRepository:
    def save(self, appointment: Appointment):
        DATABASE.append(appointment.to_dict())

    def get_all(self):
        return DATABASE