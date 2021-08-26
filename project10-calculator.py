# Project 10 - Band Name Generator
from art import logo

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1/n2

operations = {

  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide

}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))

  for key in  operations:
    print(key)

  flag = True

  while flag == True:

    operation =  input("Pick an operation?: ")

    next_num = float(input("What's the next number?: "))

    function = operations[operation] 

    answer = function(num1, next_num)

    print(f"{num1} {operation} {next_num}  = {answer}")

    exit = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()

    if exit == "n":
     flag = False
     calculator()
    else:
     num1 = answer



calculator()
