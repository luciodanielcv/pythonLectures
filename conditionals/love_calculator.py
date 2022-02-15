



print("Welcome to the love calculator!")

name1 = input("What is your name? ")
name2 = input("What is her name? ")

var_love = 0
var_true = 0
for letter in name1:
  lower = letter.lower()
  if( lower == "l" or lower == "o" or lower == "v" or lower == "e" ):
    var_love += 1
  if( lower == "t" or lower == "r" or lower == "u" or lower == "e" ):
    var_true += 1

for letter in name2:
  lower = letter.lower()
  if( lower == "l" or lower == "o" or lower == "v" or lower == "e" ):
    var_love += 1
  if( lower == "t" or lower == "r" or lower == "u" or lower == "e" ):
    var_true += 1

print(f"True letters were found {var_true} times")
print(f"Love letters were found {var_love} times")

result = var_love % 10
result += var_true * 10

if result < 10 or result > 90:
  print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
  print(f"Your score is {result}, you are alright together.")
else:
  print(f"The result is {result}")

