class Appointment:
    def __init__(self, patient_name: str, practitioner_name: str, appointment_time: str):
        self.patient_name = patient_name
        self.practitioner_name = practitioner_name
        self.appointment_time = appointment_time

    def to_dict(self):
        return {
            "patient": self.patient_name,
            "practitioner": self.practitioner_name,
            "time": self.appointment_time
        }