#6. Lambda Function
#Problem:
#Create a lambda function to compute the cube of a number.

#note , lambda fucntion means a function without a name, it is an anonymous function, it can take any number of arguments but can only have one expression.

cube = lambda x: x ** 3
x = int(input("Enter a number: "))
result = cube(x)
print(f"the cube of {x} is: {result}")

#we should have used def function instead of lambda function because lambda function is used for small functions and it is not recommended to use it for complex functions.
#lambda make it short , u dont have to write more code