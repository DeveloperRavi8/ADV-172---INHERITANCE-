class Doctor:
    def __init__(self):
        print("Doctor Class is called")

    def calculate_bmi(weight, height):
        bmi = weight / (height * height)
        print("Your BMI is : " + str(bmi) )
    
    def heart_rate(heart_rate):
        if(heart_rate > 80 and heart_rate < 100):
            print("Great your Heart Rate is normal")
        else:
            print("Your Heart rate does not seem normal. Please vist the clinc")

class Patient(Doctor):
    def __init__(self, name, weight, height, heart_rate): 
        print("Your heath report is ready")
        self.Patient_name = name
        self.Patient_weight = weight
        self.Patient_height = height
        self.heart_rate = heart_rate
    
    def healthCheck(self):
        Doctor.calculate_bmi(self.Patient_weight, self.Patient_height)
        Doctor.heart_rate(self.heart_rate)


patient1 = Patient("Ravi Kushwaha", 50, 1.6, 96)
patient1.healthCheck()
print('\n')
patient2 = Patient("Kajal Kushwaha", 50, 1.3, 64)
patient2.healthCheck()