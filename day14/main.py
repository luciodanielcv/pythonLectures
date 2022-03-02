

from art import logo
from art import vs
import os
import random
from data import data

user_score = 0

flag_continue_game = 'y'

os.system("clear")
print(logo)
first_choice = random.choice(data)
second_choice = random.choice(data)
while True:
  if second_choice["name"] != first_choice["name"]:
    break
  second_choice = random.choice(data)


print(f"Compare A: {first_choice['name']} {first_choice['description']}")
print(vs)
print(f"Against B: {second_choice['name']} {second_choice['description']}")

while flag_continue_game == 'y':

  follower_guess = input("Which has more followerds 'A' or 'B'? ")

  if follower_guess == 'A':
    if first_choice["follower_count"] < second_choice["follower_count"]:
      print("Incorrect. You lose!")
      print(f"A follower count {first_choice['follower_count']}")
      print(f"B follower count {second_choice['follower_count']}")
      print(f"Final score {user_score}")
      break
  else:
    if second_choice["follower_count"] < first_choice["follower_count"]:
      print("Incorrect. You lose!")
      print(f"A follower count {first_choice['follower_count']}")
      print(f"B follower count {second_choice['follower_count']}")
      print(f"Final score {user_score}")
      break
    else:
      first_choice = second_choice  
  
  os.system("clear")
  print(logo)
  user_score += 1
  
  print(f"You are right! Current score {user_score}")
  second_choice = random.choice(data)
  while True:
    if second_choice["name"] != first_choice["name"]:
      break
    second_choice = random.choice(data)

  print(f"Compare A: {first_choice['name']}, {first_choice['description']}, from {first_choice['country']}")
  print(vs)
  print(f"Against B: {second_choice['name']}, {second_choice['description']}, from {second_choice['country']}")

  


