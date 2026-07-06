#1. Basic Function Syntax
#Problem:
#Write a function to calculate and return the square of a number.

def square(num):  #look here SQUARE is a function, 
                #def means we are defining a function, 
                #num or u can say inside c bracket we have parameter its like placeholder
    return num ** 2 #return means u are not printing the value just the value is save for funci=tion AQUARE, AND IT WILL BE CALLED IT WILL BE PRINTED

num = int(input("Enter a number: "))

result = square(num)
print(result)
#or
print(f"the square of {num} is: {result}")

    