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