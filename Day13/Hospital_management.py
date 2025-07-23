from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact

    @abstractmethod
    def get_role(self):
        pass

class Doctor(Person):
    def __init__(self, name, age, contact, specialization):
        super().__init__(name, age, contact)
        self.specialization = specialization

    def get_role(self):
        return "Doctor"

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"

class Patient(Person):
    def __init__(self, name, age, contact, patient_id):
        super().__init__(name, age, contact)
        self.patient_id = patient_id

    def get_role(self):
        return "Patient"

    def __str__(self):
        return f"{self.name} (ID: {self.patient_id})"

class Appointment:
    def __init__(self, doctor, patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date

    def details(self):
        return f"Appointment on {self.date}:\n  Doctor: {self.doctor}\n  Patient: {self.patient}"

class Prescription:
    def __init__(self, doctor, patient, medicine_list):
        self.doctor = doctor
        self.patient = patient
        self.medicine_list = medicine_list

    def generate(self):
        meds = ", ".join(self.medicine_list)
        return (f"Prescription:\nDoctor: {self.doctor}\n"
                f"Patient: {self.patient}\nMedicines: {meds}")

class SpecialistDoctor(Doctor):
    def __init__(self, name, age, contact, specialization, years_experience):
        super().__init__(name, age, contact, specialization)
        self.years_experience = years_experience

    def get_role(self):
        return f"Specialist Doctor ({self.specialization})"

# Create doctor and patient
doc = SpecialistDoctor("Nikhil Sharma", 45, "9999988888", "Cardiology", 15)
pat = Patient("Anita Rao", 60, "8888877777", "P102")

# Book appointment
appt = Appointment(doc, pat, "2025-07-24")
print(appt.details())

# Generate prescription
pres = Prescription(doc, pat, ["Aspirin", "Atorvastatin", "Metoprolol"])
print("\n" + pres.generate())

# Show roles
print("\nRoles:")
print(f"{doc.name} is a {doc.get_role()}")
print(f"{pat.name} is a {pat.get_role()}")
