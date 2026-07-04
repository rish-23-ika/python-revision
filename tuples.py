tea = ("black", "green", "oolang", "white")
print(tea)

print(tea[0])

print(tea[-1])

print(tea[1:])

## tea[0] = "masala"  ##this will give an error because tuples are immutable, meaning their elements cannot be changed after they are created.

print(len(tea))

more_tea = ("masala", "ginger","pink")

all_tea = tea + more_tea  ##concatenating two tuples tea and more_tea to create a new tuple all_tea
print(all_tea)

if "green" in all_tea:
    print("Green tea is available.")

print()

more_tea = ("masala", "ginger","masala")
print(more_tea.count("masala"))

print(type(more_tea))

#nesting is also aloowed here