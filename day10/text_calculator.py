
from art import logo
import os

#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Substract
def substract(n1, n2):
  return n1 - n2

#Miltiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

#WTF!
#function = operations["*"]
#print(function(2, 3))

print(logo)
num1 = float(input("What is the first operand? "))

continue_calculation = "y"
while continue_calculation == "y":

  for op in operations:
    print(op)

  operation_symbol = input("Pick an operation from the line above: ")

  num2 = float(input("What is the next operand: "))

  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")

  continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit: ")
  if continue_calculation == 'n':
    os.system("clear")
    print(logo)
    num1 = float(input("What is the first operand? "))

    continue_calculation = "y"

  else:
    num1 = answer




