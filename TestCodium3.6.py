# 3.6

numbers = int(input("Enter a number : "))

spaceAB = numbers - 1
space_in = -1
part_one = numbers

for row in range(part_one):
    txt = ""
    for space_A_do in range(spaceAB):
        txt += "A"

    txt += "+"

    for space_inside_do in range(space_in):
        txt += "E"

    if row > 0:
        txt += "+"

    for space_B_do in range(spaceAB):
        txt += "B"

    spaceAB -= 1
    space_in += 2
    print(txt)

spaceCD = 1
part_two = numbers - 1
space_in -= 4

for row in range(part_two):
    txt = ""
    for space_C_do in range(spaceCD):
        txt += "C"

    txt += "+"

    for space_inside_do in range(space_in):
        txt += "E"

    if row < (part_two - 1):
        txt += "+"

    for space_D_do in range(spaceCD):
        txt += "D"

    spaceCD += 1
    space_in -= 2
    print(txt)