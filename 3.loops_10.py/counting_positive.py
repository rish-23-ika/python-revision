#1. Counting Positive Numbers
#Problem:
#Given a list of numbers, count how many are positive.

#numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

count = 0

n = int(input("How many numbers do you want to enter?: "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))

    if num > 0:
        count += 1

print(f"Total positive numbers are: {count}")