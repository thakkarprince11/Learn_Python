
# Determine if a year is leap year. (Leap years are divided by 4, but not by 100 unless also divisible by 400).


year = int(input("Enter a year : "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
    print(year, " is a leap year")
else:
    print(year, "is NOT a leap year")



