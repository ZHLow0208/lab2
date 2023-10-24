def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi = weight/height**2
 print(str(bmi))
calculate_bmi(weight=57, height=1.73)