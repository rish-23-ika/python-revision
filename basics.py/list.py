teas = ["black", "green", "oolang", "white"]
print(teas)
print(teas[-1])
print(teas[1])

print(teas[1:2])
teas[1:2] = ["Lemon"]
print(teas)

teas[1:3] = ["pink", "blue"]
print(teas)

print(teas[1:1])
teas[1:1] = ["yellow"]
print(teas)

teas[1:3] = []
print(teas)

for tea in teas:
    print(tea, end="-" )


print()          # move cursor to next line otherwise both code will be printed in the same line

print(teas)

teas.append("masala")

if "masala" in teas:
    print("Masala tea is available.")

print(teas)

if "green" not in teas:
    print("Green tea is not available.")

if "green" in teas:
    print("Green tea is available.")

if "white" in teas:
    print("White tea is available.")


teas.pop()  ##removes the last element from the list teas
print(teas)

teas.remove("blue")  ##removes the first occurrence of the element "pink" from the list teas
print(teas)

teas.insert(1, "green")  ##inserts the element "green" at index 1 in the list teas
print(teas)

teas_copy = teas.copy()  ##creates a shallow copy of the list teas and assigns it to the variable teas_copy
print(teas_copy)

teas_copy.append("herbal")  ##appends the element "herbal" to the end of the list teas_copy
print(teas_copy)
print(teas)  ##prints the original list teas, which remains unchanged after modifying teas_copy

squared_num = [x**2 for x in range(10)]  ##creates a new list squared_num that contains the squares of numbers from 0 to 10 using a list comprehension
print(squared_num)

cube_num = [x**3 for x in range(7)]  ##creates a new list cube_num that contains the cubes of numbers from 0 to 7 using a list comprehension
print(cube_num)