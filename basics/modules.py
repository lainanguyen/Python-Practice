import modules_converter
from utils import find_max

from modules_converter import kg_to_lbs
# When we import a specific function from our module, we can easily call that function without prefixing module name
kg_to_lbs(100)

print(modules_converter.lbs_to_kg(70))

# Challenge
# Using utils.py

numbers = [10, 3, 6, 2]
print(find_max(numbers))
