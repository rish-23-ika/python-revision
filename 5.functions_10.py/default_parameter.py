#5. Default Parameter Value

#Problem:
#Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(user_name):
    if user_name:
        return(f"Hello, {user_name}!")
    else:
        return("Hello, Guest!")

user_name = input("Enter your name (or press Enter to skip): ")
greeting = greet(user_name)
print(greeting)