import time
BodyFatValue = [] # array

Sex = input("Enter your gender(m for male, f for female): ")

EnumerationNumber = 1
for i in range(EnumerationNumber): #for loop
  if Sex == "m": # if statement
    try: 
      Chest = float(input("Please enter the Chest skinfold in mm: "))
      Abdomen = float(input("Please enter your Abdomen skinfold in mm: "))
      Thigh = float(input("Please enter your Thigh skinfold in mm: "))
      X3 = float(input("Please enter your age: "))
      X4 = float(input("Please enter your waist circumference in mm: "))
      X2 = Chest + Abdomen + Thigh
      X5 = float(input("Enter your forearm circumference in mm: "))
      BodyDensity = 1.0990750 - 0.0008209 * X2 + 0.0000026 * X2 * 2 - 0.0002017 * X3 - 0.005675 * X4 + 0.018586 * X5
      bFat = 495/BodyDensity - 450
      BodyFatValue.append(bFat) #push function
      print("Your body fat percentage value is", BodyFatValue[0], "%")
    except ValueError:
      print("Please enter an integer")  
  elif Sex == "f":
    try:
      Triceps = float(input("Please enter the triceps skinfolds in mm: "))
      Thigh = float(input("Please enter the size of the thigh skinfold in mm: "))
      Suprailiac = float(input("Please enter the size of the suprailiac skinfold in mm: "))
      Age = float(input("Please enter your age: "))
      X5 = float(input("Enter your gluteal circumference in cm: "))
      X3 = Thigh + Triceps + Suprailiac
      X4 = Age
      BodyDensity = 1.1470292 - 0.0009376 * X3 + 0.0000030 * X3 * 2 - 0.0001156 * X4 - 0.0005839 * X5
      bFat = 495/BodyDensity - 450
      BodyFatValue.append(bFat)
      print("Your body fat percentage value is", BodyFatValue[0], "%")
    except ValueError:
      print("Please enter an integer")
  else:
    print("Invalid value try again")
    time.sleep(1)
    exit()

