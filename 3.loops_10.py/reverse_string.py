#4. Reverse a String
#Problem:
#Reverse a string using a loop.

string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(f"The reversed string is: {reversed_string}")


#or

string = input("Enter a string: ")
print(string[::-1])