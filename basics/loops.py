# While loops
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("done")


# For loops

for item in 'Python':
    print(item)

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

# Range function

for item in range(5, 10, 2):
    print(item)

prices = [10, 20, 30]
total = 0
for i in prices:
    total += i
    print(f"Total: {total}")


# Nested loop

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

# Challenge
# Do not use i * x, use nested loop
# i        0  1  2  3  4
numbers = [5, 2, 5, 2, 2]   # No. of x's on each line
for i in numbers:
    output = ''
    for j in range(i):
        output += 'x'
    print(output)

print("\n")

l_numbers = [2, 2, 2, 2, 5]
for i in l_numbers:
    output = ''
    for j in range(i):
        output += 'x'
    print(output)

