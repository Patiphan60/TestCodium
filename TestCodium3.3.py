# 3.3

numbers = int(input(" Enter Numer = "))
for row in range(1, numbers+1):
    for column in range(1, numbers-row + 1):
        print(" ", end="")
    for column in range(1, 2 * row):
        if column == 1 or column == 2 * row-1:
            print("*", end="")
        else:
            print("", end=" ")
    print(" ")


