
#Import module
import random

#Print title
print("Who is paying?")

#List of people
people = input("Please type the names separated by commas: ")

#Remove spaces in the string
people = people.replace(" ", "")

#Split string into a list
peopleList = people.split(",")

#Choice someone at random
payer = random.choice(peopleList)

#The payer
print(f"The payer of the bill is: {payer}")

