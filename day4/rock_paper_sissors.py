
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock, paper, scissors]

your_choice = input("Your choice is (rock=0, paper=1, scissors=2)? ")
your_choice = int(your_choice)
computer_choice = random.randint(0,2)


if your_choice > 2:
  print("You typed an invalid number, you lose!")
else:
  print(f"Your choice {your_choice}")
  print(options[your_choice])

  print(f"Computer's choice {computer_choice}")
  print(options[computer_choice])

  if your_choice == computer_choice:
    print("It is a draw")
  elif your_choice == 0 and computer_choice == 1:
    print("Computer wins")
  elif your_choice == 0 and computer_choice == 2:
    print("You win")
  elif your_choice == 1 and computer_choice == 0:
    print("You win")
  elif your_choice == 1 and computer_choice == 2:
    print("Computer wins")
  elif your_choice == 2 and computer_choice == 0:
    print("Computer wins")
  elif your_choice == 2 and computer_choice == 1:
    print("You win")

