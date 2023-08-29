# -*- coding: utf-8 -*-
"""codsoft internship.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g0obcohsgP_KTvReyEGunwl5QFshnSdj
"""

def add(num1, num2):
  """Adds two numbers."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts two numbers."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers."""
  return num1 * num2

def divide(num1, num2):
  """Divides two numbers."""
  return num1 / num2

def main():
  """The main function."""
  print("Welcome to the simple calculator!")

  # Get the two numbers from the user.
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  # Get the operation choice from the user.
  operation = input("Enter the operation (+, -, *, /): ")

  # Perform the calculation.
  if operation == "+":
    result = add(num1, num2)
  elif operation == "-":
    result = subtract(num1, num2)
  elif operation == "*":
    result = multiply(num1, num2)
  elif operation == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operation!")
    return

  # Display the result.
  print("The result is", result)

if __name__ == "__main__":
  main()