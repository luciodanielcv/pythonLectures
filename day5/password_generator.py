#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#Hard level ->
tipos_caracteres = ["letter", "symbol", "number"]
total_caracteres = nr_letters + nr_symbols + nr_numbers

random_password = ""
for n in range(1,total_caracteres+1):
  caracter = random.choice(tipos_caracteres)

#If letter or symbol or number
#Then generate the random character and append it to the random_password
#Remove one position to the letter list or symbol list or number list
  if caracter == "letter":
    random_password += random.choice(letters)
    nr_letters -= 1
  elif caracter == "symbol":
    random_password += random.choice(symbols)
    nr_symbols -= 1
  else:
    random_password += random.choice(numbers)
    nr_numbers -= 1


#Check if letters or symbols or numbers were exhusted
#If exhusted, discard them for the rest of the password
  if "letter" in tipos_caracteres and nr_letters <= 0:
    tipos_caracteres.remove("letter")
  if "symbol" in tipos_caracteres and nr_symbols <= 0:
    tipos_caracteres.remove("symbol")
  if "number" in tipos_caracteres and nr_numbers <= 0:
    tipos_caracteres.remove("number")
  
print(f"The final password is this: {random_password}")


### PD: Jajaja shuffle function was not allowed
# =V

