# Dictionaries

"""
Key value pairs
Keys    Values
Name:   John Smith
Email:  john@gmail.com
Phone:  1234
"""

customer = {
    "name": "John Smith",
    "age": 30,
    # "age": 40,    This is not allowed, as key should be unique
    "is_verified": True
}

# Accessing values
print(customer["name"])
# print(customer["Name"])   Throws an error because key is not exactly the same
print(customer.get("Name"))  # Will not throw error but will return None

# Updating values
print(customer.get("birthdate", "Jan 1 1980"))  # Second parameter supplies default value
customer["name"] = "Jack Smith"
print(customer["name"])
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])
print(customer)

# Challenge

phone = input("Phone: ")
phone_book = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for i in phone:
    output += phone_book.get(i, "!") + " "
print(output)