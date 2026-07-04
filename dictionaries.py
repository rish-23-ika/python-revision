tea_types = {"masala": "spicy", "ginger": "cold", "white": "eww", "green": "healthy"}
print(tea_types)

print(tea_types["masala"])

print(tea_types.get("ginger"))

tea_types["green"] = "healthy and refreshing"
print(tea_types)

for tea in tea_types:
    print(tea, tea_types[tea])

#or

for key, value in tea_types.items():
    print(key, value)

if "masala" in tea_types:
    print("Masala tea is available.")

print(len(tea_types))

tea_types["oolong"] = "fruity"
print(tea_types)

tea_types.pop("ginger")  ##removes the key-value pair with the key "ginger" from the dictionary tea_types
                            ##in this case, it will remove the entry "ginger": "cold" from the dictionary. 
                            #not like list where we remove the last element. here we remove the key-value pair with the specified key.
print(tea_types)

tea_types.popitem()  ##removes last element from the dictionary tea_types. 
                        #In this case, it will remove the last key-value pair added to the dictionary, which is "oolong": "fruity".
print(tea_types)

del tea_types["white"]  ##removes the key-value pair with the key "white" from the dictionary tea_types
print(tea_types)

tea_types_copy = tea_types.copy()  ##creates a shallow copy of the dictionary tea_types and assigns it to the variable tea_types_copy

print()

tea_shop = {
    "tea": {"masala": "spicy", "ginger": "cold", "white": "eww", "green": "healthy"},
    "chai": {"black": "strong", "pink": "refreshing", "oolong": "fruity"}
}
print(tea_shop)

print(tea_shop["tea"])

print(tea_shop["tea"]["green"])  ##accessing the value associated with the key "green" in the nested dictionary tea_shop["tea"].

squared_num = {x: x**2 for x in range(6)}  ##creates a dictionary squared_num where the keys are numbers from 0 to 5 and the values are their squares.
print(squared_num)

squared_num.clear()  ##removes all key-value pairs from the dictionary squared_num, making it an empty dictionary.



keys = ["masala", "ginger", "white", "green"]
print(keys)

default_value = "delicious"

new_dict = dict.fromkeys(keys, default_value)  ##creates a new dictionary new_dict with the keys from the list keys and assigns the default value "delicious" to each key.
print(new_dict)

new_dict = dict.fromkeys(keys, keys)  ##creates a new dictionary new_dict with the keys from the list keys and assigns the list keys itself as the value for each key.
print(new_dict)
