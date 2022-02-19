

import random
import hangman_words
from hangman_art import logo, stages
import os

#Step 4

import random

#Step 1 
#word_list = ["aardvark", "baboon", "camel"]
attemps = len(stages) - 1



#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
the_word = random.choice(hangman_words.word_list)
print(f"This is the word: {the_word}")

display = []
for _ in the_word:
  display += "_"

#Begin loop
end_of_game = False
while not end_of_game and attemps >= 0:

  os.system('clear')
  print(logo)
  print(stages[attemps])
  print(display)
  if attemps == 0:
    break

  #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  the_guess = input("Please make a guess letter: ")

  #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  if( the_word.find(the_guess) == -1 ):
    print(f"Incorrect! '{the_guess}' is not part of the word")
    attemps -= 1

  #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
  #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

  for position in range(len(the_word)):
    if the_guess.find(the_word[position]) != -1:
      display[position]=the_word[position]

  
  if "_" not in display:
    end_of_game = True

#Have you won?
print("Game Over!")
if "_" not in display:
  print(display)
  print("You won!")
else:
  print("You lose!")
  print(f"You could not guess the word {the_word}")
