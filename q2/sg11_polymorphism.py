#Activity 1
class Patient: 
 ## initializes the patient's name and their bill amount
    def__init__(self, name, bill_amount): 
       self.name = name 
       # stores the patient's name
       self.bill_amount = bill_amount
       # stores their bill amount

    def get_name(self): 
       return self.name

    def set_name(self,name):
       self.name = name

    def get_bill_amount(self,bill_amount):
       return self.bill_amount

    def set_bill_amount(self,bill_amount):
       self.bill_amount = bill_amount

    def calculate_bill(self):
       return self.bill_amount

    def display_patient_type(self):
       print("Patient Type: Regular Patient")

class PhilHealthPatient(Patient):
    def calculate_bill(self):
    # multiplies to 0.80 or 80%
       return self.bill_amount*0.85

    def display_patient_type(self):
       print("Patient Type: Senior Citizen")
  
class PhilHealthPatient(Patient):
    def calculate_bill(self):
    # multiplies to 0.85 or 85%
       return self.bill_amount*0.85
  
    def display_patient_type(self):
       print("Patient Type: PhilHealth Member")

print("Hospital Billing System")
print ("-----------------------")

# creates the object for patient 1
patient 1 = Patient("Juan Dela Cruz, 15000")
print("\nPatient Name: ", patient1.get_name())
patient1.display_patient_type()
print(f"Original Bill: ₱{patient1.get_bill_amount():.2f}")
print(f"Final Bill: ₱{patient1.calculate_bill():.2f}")

# creates the object for patient 2
patient 2 = Senior("Maria Santos, 15000")
print("\nPatient Name: ", patient2.get_name())
patient2.display_patient_type()
print(f"Original Bill: ₱{patient2.get_bill_amount():.2f}")
print(f"Final Bill: ₱{patient2.calculate_bill():.2f}")

# creates the object for patient 3
patient 3 = PhilHealthPatient("Pedro Reyes", 15000)
print("\nPatient Name: ", patient3.get_name())
patient3.display_patient_type()
print(f"Original Bill: ₱{patient3.get_bill_amount():.2f}")
print(f"Final Bill: ₱{patient3.calculate_bill():.2f}")



    
