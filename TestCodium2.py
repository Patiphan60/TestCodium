# 2

year = int(input("Year = "))

if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    print(year, True)

else:
    print(year, False)









