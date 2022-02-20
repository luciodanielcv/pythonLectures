
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
  the_ciphered_text = ""
  for letter in text:
    index = alphabet.index(letter)
    new_position = index+shift
    new_position = new_position % len(alphabet)
    the_ciphered_text += alphabet[new_position]
  print(f"The ciphered text is {the_ciphered_text}")

def decrypt(text, shift):
  the_plain_text = ""
  for letter in text:
    index = alphabet.index(letter)
    new_position = index-shift
    #new_position = new_position % len(alphabet)
    the_plain_text += alphabet[new_position]
  print(f"The plain text is {the_plain_text}")

def caesar(text, shift, operation):
  end_text = ""
  if operation == "decode":
    shift *= -1
  for letter in text:
    if letter.isalpha():
      index = alphabet.index(letter)
      new_position = index+shift
      new_position = new_position % len(alphabet)
      end_text += alphabet[new_position]
    else:
      end_text += letter
  print(f"The end text is {end_text}")

print(logo)

still_ciphering = True
while still_ciphering:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)

  keep_ciphering = input("Still ciphering (Y/N)? ")
  if keep_ciphering.lower() == "n":
    still_ciphering = False

print("Good bye")