# Short strings

course = "Python for Beginners"
course1 = 'Python "for" Beginners'
print(course)
print(course1)


# Long strings
# Use triple quote (''') for multi lines

course2 = '''
Hi John,

Here is our first email to you. 

Thank you, 
The support team
'''
print(course2)


# Index
# First letter starts with 0
# Negative values with work backwards

course3 = 'Python for Beginners'
print(course3[0])
print(course3[-1])
print(course3[0:3])  # Display only a set of values
print(course[3:10])  # Will print all values from 3 to 9
another = course3[:]  # Prints all values
print(another)

name = "Jennifer"
print(name[1:-1])
# Will print ennife


# Formatted Strings

# Printing out John [Smith] is a coder.
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] ' + "is a coder."
print(message)

# Better way to do the above^
first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a coder.'  # Curly braces {} allow for holes in string for value of variables
print(msg)


# String methods

course4 = 'Python for Beginners'

print(len(course4))  # len() counts the no. of letters

print(course4.upper())  # .upper() capitalizes letters
print(course4.lower())  # .lower() de-capitalizes letters

print(course4.find('o'))  # Finds where a letter is

print(course4.replace('e', 'a'))  # Replaces first value with second value in parameter

print('Python' in course4)  # Checks to see if declared string is in variable, boolean value