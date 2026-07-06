#7. Function with *args
#Problem:
#Write a function that takes a variable number of arguments and returns their sum.


#Quick memory trick:

        #*args → many values → stored as a tuple
        #**kwargs → many named values → stored as a dictionary

def add_numbers(*args):
    return sum(args)

print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(10, 20, 30, 40))

#"Accept any number of arguments and store them in a tuple called args."

#For example:
#add_numbers(10, 20, 30)

#Inside the function:
#args = (10, 20, 30)