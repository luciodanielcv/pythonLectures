

height = input("Enter your height in meters ")
weight = input("Enter your weight in kilograms ")


bmi = float(weight) / (float(height) ** 2 )
bmi_as_int = int(bmi)
print( "Your bmi is " + str(bmi_as_int))

