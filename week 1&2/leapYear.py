# program to check if the year is leap or not

year = int(input("Enter a year: "))
if (year % 4 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
