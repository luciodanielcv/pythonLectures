

import random
import os


game_difficulty = {
  "easy": 15,
  "normal": 10,
  "hard": 5
}

continue_game = 'y'
while continue_game == 'y':
  os.system("clear")
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  secret_number = random.randint(1,100)

  game_type = input("Choose a difficulty. Type 'easy', 'normal' or 'hard': ")

  attempts = game_difficulty[game_type]

  while attempts > 0:
    print(f"You have {attempts} remaining to guess a number.")
    guess_number = int(input("Make a guess: "))

    if guess_number == secret_number:
      print(f"You have won! The secret number is {secret_number}")
      break

    attempts -= 1
    if guess_number < secret_number:
      print("Too low.")
    else:
      print("Too high.")
  
  if attempts == 0:
    print("You could not guess the secret number. You lose!")
    print(f"The secret number is this: {secret_number}")
  continue_game = input("Restart game y/n? ")

