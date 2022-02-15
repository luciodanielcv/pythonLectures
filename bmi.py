

height = input("Enter your height in meters ")
weight = input("Enter your weight in kilograms ")


bmi = float(weight) / (float(height) ** 2 )
bmi_as_int = round(bmi)

if bmi_as_int < 18.5:
  print(f"Your bmi is {bmi_as_int}. You are underweight")
elif bmi_as_int < 25:
  print(f"Your bmi is {bmi_as_int}. You have a normal weight")
elif bmi_as_int < 30:
  print(f"Your bmi is {bmi_as_int}. You are overweight")
elif bmi_as_int < 35:
  print(f"Your bmi is {bmi_as_int}. You are obese")
else:
  print(f"Your bmi is {bmi_as_int}. You are clinically obese")

