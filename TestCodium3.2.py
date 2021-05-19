# 3.2

number=int(input("Enter Number = "))

for row in range(1,number+1) :
    for column in  range(number -row):
        print(" ",end=" ")
    for column in range(1,row + 1):
        print("*",end=" ")
    print(" ")

