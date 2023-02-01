# Lists

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[0])  # John
print(names[-2])  # Sarah
print(names[2:4])
names[0] = 'Jon'    # Change value in index
print(names[:])

# Challenge: Write a program to find the largest number in a list
numbers = [3, 5, 1, 9, 2, 6, 2, 5]
max_number = numbers[0]
for i in numbers:
    if i > max_number:
        max_number = i
print(max_number)


# 2D Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])
matrix[0][0] = 20
print(matrix[0][0])

matrix[0][0] = 1
for j in matrix:    # j is row
    for i in j:     # i is the inner value
        print(i)


# List Methods

numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 10)  # first value indicates index placement, second value indicates value to insert
numbers.remove(5)  # removes item at this index
# numbers.clear() # removes all values
numbers.pop()  # removes last value
print(numbers.index(2))  # index of first item with this value
print(50 in numbers)    # like the index method but doesn't throw an error, is a boolean value
print(numbers.count(1))     # Counts how many of this value there are
numbers.sort()  # Sort list
numbers.reverse()  # Sort list in descending order
numbers2 = numbers.copy()   # Make a copy of a list
numbers2.append(10)
print(numbers)
print(numbers2)

# Write a program to remove the duplicates in a list
number_list = [2, 4, 5, 5, 2, 9, 1]
unique = []
for i in number_list:   # i is number
    if i not in unique:
        unique.append(i)
print(unique)
# We solved this problem through creating another list to filter through the values


# Tuples: Like list but unchangeable

numbers3 = (1, 2, 3)
# numbers3[0] = 3  # This will throw an error because tuples don't support item assignment
print(numbers3[0])

# Unpacking

coordinates = (1, 2, 3)

# Long way:
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# Short way:
x, y, z = coordinates
print(y)

