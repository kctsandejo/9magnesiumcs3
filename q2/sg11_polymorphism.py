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
    def display_patient_type(self):
    

class PhilHealthPatient(Patient):
    def calculate_bill(self):
    # multiplies to 0.85 or 85%
       return self.bill_amount*0.85
  
    def display_patient_type(self):
       print("Patient Type: PhilHealth Member")

print("Hospital Billing System")
print ("-----------------------")

patient 1 = Patient("Juan Dela Cruz, 15000")


    
