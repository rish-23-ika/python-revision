#9. Leap Year Checker
#Problem:
#Determine if a year is a leap year.

#Rules:
#- A leap year is divisible by 4
#- But not divisible by 100
#- Unless it is also divisible by 400

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")