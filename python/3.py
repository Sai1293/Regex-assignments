kg = float(input("Enter your weight in kgs : "))
mtrs = float(input("Enter your height in mtrs : "))

bmi = kg / (mtrs * mtrs)

print("your bmi : ", bmi)

if (bmi < 18.5):
    print("Underweight")
elif (bmi > 18.5 and bmi < 25):
    print("Normal")
elif (bmi > 25 and bmi < 30):
    print("Overweight")
elif(bmi >= 30):
    print("Obese")
