# Functions
def greet_user():
    print("Hello there!")
    print("Welcome aboard")


print("Start")
greet_user()
print("Finish")


# Parameters
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard!')


greet_user("John", "Smith")
greet_user("Mary", "Smith")


# Keyword arguments
# Positional of arguments doesn't matter
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard!')


greet_user(last_name="Smith", first_name="Bob")


