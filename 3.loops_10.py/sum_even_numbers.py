#2. Sum of Even Numbers
#Problem:
#Calculate the sum of even numbers up to a given number n.

sum_even = 0
n = int(input("Enter a number: "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        sum_even += num

print(f"The sum of even numbers is: {sum_even}")
