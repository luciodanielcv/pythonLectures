


print("Welcome to the rollercoster!")

height = int(input("How much tall are you (cms)? "))
age = int(input("How old are you (years)? "))

bill = 0
if height >= 120:
  print("You can ride the rollercoster!")
  if age < 12:
    bill = 5
    print("Child pay $5")
  elif age <= 18:
    bill = 7
    print("Youth pay $7")
  elif age < 45:
    bill = 12
    print("Adult pay $12")
  elif age <= 55:
    bill = 0
    print("Adult age between 45 and 55")
  else:
    bill = 12
    print("Adult pay $12")
  
  wants_photo = input("Do you want a photo taken. Y or N? ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")
else:
  print("Sorry you have to be taller.")

