# 9. Generator Function with yield
#Problem:
#Write a generator function that yields even numbers up to a specified limit.

def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

num = int(input("Enter the limit: "))

for number in even_numbers(num):
    print(number)