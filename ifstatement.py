# IF statement

"""
If it's hot
    It's a hot day
    Drink plenty of water
Otherwise if it's cold
    It's a cold day
    Wear warm clothes
Otherwise
    It's a lovely day
"""

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")


"""
Price of a house is $1M.
If buyer has good credit, 
    they need to put down 10%
Otherwise
    they need to put down 20%
Print the down payment
"""

good_credit = False

if good_credit:
    down_payment = ((1/100)*10)*1000000
    print(f"You need to pay ${down_payment}")
else:
    down_payment = ((1/100)*20)*1000000
    print(f"You need to pay ${down_payment}")
