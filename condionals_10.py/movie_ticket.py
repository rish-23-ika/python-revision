#2. Movie Ticket Pricing
#Problem:
#Movie tickets are priced based on age:
#- $12 for adults (18 and over)
#- $8 for children
#- Everyone gets a $2 discount on Wednesday

age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").strip().lower()
            #This way it handles: This way it handles: Wednesday, wednesday, WEDNESDAY, WeDnEsDaY without extra conditions.

if age >= 18:
    price = 12
else:
    price = 8

if day == "wednesday":
    price -= 2

print(f"Your ticket price is ${price}")