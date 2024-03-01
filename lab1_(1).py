# -*- coding: utf-8 -*-
"""Lab1 (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E4QWN-rm2EcfJiIjo9h-GNN-2VZNRGTx

1. Write a Python program that prompts the user for their name and then prints a personalized greeting message.
"""

# Prompt the user to enter their name
name = input("Enter your name: ")

# Print a personalized greeting message
print("Hello,", name + "!")

"""Exercise 1. <br />
Ask 3 questions about the name, surname and age, and at the end create a sentence with this information.
"""

name = input("Enter your name")
surname = input("Enter your surname")
age = input("Enter your age")

print(name, surname, age)

"""2. Write a Python program that converts temperature from Celsius to Fahrenheit."""

celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print the converted temperature
print("Temperature in Fahrenheit:", fahrenheit)

"""Exercise 2. <br />
Reverse to change Fahrenheit to Celsius.
"""

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * (5/9)

# Print the converted temperature
print("Temperature in Celsius:", celsius)

"""3. Write a Python program that calculates the grade based on the student's score."""

# Define variable
score = float(input("Enter your score: "))

# Determine the grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print the grade
print("Your grade is:", grade)

"""Exercise 3. <br />
Convert to the Polish grading system.
"""



"""4. Write a Python program that checks if a number is even or odd."""

# Define variable
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

# Print the result
print("The number is:", result)

"""Exercise 4. <br />
Change the code so that there are two inputs and the first number it can be devidet.
"""



"""5. Variable types"""

# Prompt the user to enter values of different types
var_int = int(input("Enter an integer value: "))
var_float = float(input("Enter a float value: "))
var_str = input("Enter a string value: ")
var_bool = input("Enter a boolean value (True or False): ").lower() == "true"

# Determine the type of each variable
type_int = type(var_int).__name__
type_float = type(var_float).__name__
type_str = type(var_str).__name__
type_bool = type(var_bool).__name__

# Print the type of each variable
print("Type of var_int:", type_int)
print("Type of var_float:", type_float)
print("Type of var_str:", type_str)
print("Type of var_bool:", type_bool)

"""6. Write a Python program that determines the type of triangle based on the lengths of its sides."""

# Define variables
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check the type of triangle
if side1 == side2 == side3:
    triangle_type = "Equilateral"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = "Isosceles"
else:
    triangle_type = "Scalene"

# Print the type of triangle
print("The triangle is:", triangle_type)

"""Exercise 6. <br />
Add a check to see if a triangle can be drawn with the given sides.
"""



"""7. Write a Python program that performs arithmetic operations on two numbers."""

# Define variables
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

# Print the result
print("Result:", result)

"""Exercise 7. <br />
Add a check to see if someone is trying to divide by zero, if so, give an appropriate message
"""



"""Exercise 8. <br />
Make a script out of all task and put it on githyb
"""

