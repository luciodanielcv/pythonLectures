
print("Leap years!")

year = int(input("Which year do you want to check? "))

#If year is divisible by 4
if year % 4 == 0:
  #Except year is divisible by 100
  if year % 100 == 0:
    #Unless year is divisible by 400
    if year % 400 == 0:
      #It is leap year
      print(f"The year {year} is a leap year!")
    else:
      #It is not leap year
      print(f"The year {year} is NOT leap year!")
  else:
    #Divisible by 4 but not by 100
    print(f"The year {year} is leap year!")
else:
  #Not divisible by 4. Not leap year
  print(f"The year {year} is NOT leap year!")
