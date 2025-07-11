height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print("\n📊 BMI Report")
print("-------------------------")
print(f"Height       : {height} m")
print(f"Weight       : {weight} kg")
print(f"BMI          : {bmi:.2f}")
print(f"Category     : {category}")
