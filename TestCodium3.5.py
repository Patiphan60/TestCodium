# 3.5

numbers = int(input("Enter Number: "))
row = 12
for row in range(numbers + 1):
    if row % 2 != 0:
        sum1 = (numbers - row) // 2
        print(" " * sum1 + "*" * row + " " * sum1, end="\n")


column = 1
for column in range(numbers - 1, 0, -1):
    if column % 2 != 0:
        sum2 = (numbers - column) // 2
        print(" " * sum2 + "*" * column + " " * sum2, end="\n")

