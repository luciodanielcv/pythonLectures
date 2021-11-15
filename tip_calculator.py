

print("Welcome to the tip calculator")

bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give (10, 12 or 15)? ")
people = input("How many people to split the bill? ")

tip_by_person = (int(percentage)/100) * float(bill)/int(people)
tip_by_person = round(tip_by_person, 2)
bill_by_person = float(bill)/int(people)
print(f"A person bill is {bill_by_person:.2f}" )
print(f"Tip by person is {tip_by_person:.2f}")

