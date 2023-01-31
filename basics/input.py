# Input function takes input from user and returns it as an output

name = input('What is your name? ')
print('Hi ' + name)

fav_color = input("What's your favorite color? ")
print(name + " likes " + fav_color)

# Type conversion

# int() - converts string into integer
# float() - converts string into integer with decimal
# bool() - converts string into boolean value (True/False)

birth_year = input("Birth year: ")
age = 2023 - int(birth_year)
print(age)

# Exercise
# Ask a user their weight (in pounds), convert it to kilograms and print on the terminal.

weight_in_lbs = input("What is your weight in lbs? ")
weight_in_kg = 0.454 * float(weight_in_lbs)
print(weight_in_kg)