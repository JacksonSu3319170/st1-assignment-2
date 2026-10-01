from repositories import AppointmentRepository
from services import AppointmentService


def main():
    repo = AppointmentRepository()
    service = AppointmentService(repo)

    print("Welcome to SmartCare: The Clinical Appointment Booking System!")

    # Book appointments
    service.book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
    service.book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')

    # Display appointments
    appointments = service.get_appointments()
    if not appointments:
        print("No appointments recorded.")
        return

    for appt in appointments:
        print(f"Patient: {appt['patient']} | Practitioner: {appt['practitioner']} | Time: {appt['time']}")


if __name__ == "__main__":
    main()