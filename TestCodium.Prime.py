# prime

numbers = int(input(" Enter Number = "))
print(numbers, " -> ", end=" ")

for row in range(numbers+1):
    if row > 1:
        for column in range(2, row):
            if (row % column) == 0:
                break
        else:
            print(row, end=" ")






