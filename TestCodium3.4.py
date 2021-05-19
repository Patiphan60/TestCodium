# 3.4

numbers = int(input("Enter Number : "))
asterisk = int(numbers / 2)
temp = 0 if numbers % 2 == 0 else 1
space = 0
space_in = numbers - 2
for row in range(asterisk):
    txt = ""
    print((" " * space) + "*" + (" " * space_in) + "*" if numbers > 1 else "")

    space += 1
    space_in -= 2

txt = (" " * asterisk) + "*" if temp == 1 else ""
if txt:
    print(txt)

space = asterisk - 1
space_in = 0 if numbers % 2 == 0 else 1
for row in range(asterisk):
    txt = ""
    print((" " * space) + "*" + (" " * space_in) + "*" if numbers > 1 else "")

    space -= 1
    space_in += 2