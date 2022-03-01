

#global variable
enemies = 1

def increase_enemies():

  #Local variable
  enemies = 2
  print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

# Functions can be nested
# The same apply for nested functions.
# Local and Global functions exist!


#For constants the naming is upper-case
PI = 3.14159

