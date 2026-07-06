#8. Function with **kwargs
#Problem:
#Create a function that accepts any number of keyword arguments and prints them in the format:
#key: value

#Quick memory trick:

        #*args → many values → stored as a tuple
        #**kwargs → many named values → stored as a dictionary

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

key = input("Enter a key: ")
value = input("Enter a value: ")
print_details(**{key: value})

#**kwargs means:

#Accept any number of keyword arguments and store them in a dictionary.

#Example:

#print_details(name="Rishika", age=19)

#Inside the function:

#kwargs = {
#    "name": "Rishika",
#    "age": 19
#}

#So:

#for key, value in kwargs.items():