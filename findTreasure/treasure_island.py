
print("Welcome to the Treasure island.")
print("Your mission is to find the treasure.")

leftright = input("Which direction do you want to take (left/right)? ").lower()

if leftright == "right":
  print("You fell into a hole. Game over!")
else:
  swimwait = input("Do you want to swim or wait (swim/wait)? ").lower()
  if swimwait == "swim":
    print("Not the best choice. Game over!")
  else:
    door = input("Which door (blue/red/yellow)? ").lower()
    if door == "blue" or door == "red":
      print("Incorrect door. Game over!")
    else:
      print("Incredible!!! You've just have won!")

