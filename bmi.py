def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi = weight/height**2
 print(str(bmi))
 if bmi < 18.5:
  return -1
 elif bmi > 25:
  return 1
 else:
  return 0
calculate_bmi(weight=57, height=1.73)