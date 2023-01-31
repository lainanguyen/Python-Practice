# Logical Operators

has_high_income = False
has_good_credit = True
has_criminal_record = False

# and
if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# or
if has_high_income or has_good_credit:
    print("Eligible for loan")

# and not
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")


# Comparison Operators

temperature = 35

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day.")


"""
If name is less than 3 characters long
    name must be at least 3 characters
Otherwise if it's more than 50 characters long
    name can be a maximum of 50 characters
Otherwise
    name looks good!
"""

name_characters = len(input("What is your name? "))

if name_characters < 2:
    print("Name must be at least 3 characters")
elif name_characters > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")