user_weight = float(input("Weight: "))
lbs_or_kg = input("(L)bs or (K)g: ")

if lbs_or_kg.upper() == "L":
    lbs_conversion = user_weight * 0.454
    print(f"You are {lbs_conversion} kilograms.")
elif lbs_or_kg.upper() == "K":
    kg_conversion = user_weight * 2.2
    print(f"You are {kg_conversion} pounds.")