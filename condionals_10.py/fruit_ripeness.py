#4. Fruit Ripeness Checker
#Problem:
#Determine if a fruit is ripe, overripe, or unripe based on its color.

#Example:
#Banana:
#- Green  → Unripe
#- Yellow → Ripe
#- Brown  → Overripe

fruit = input("Enter the fruit name: ").strip().lower()
if fruit == "banana":
    color = input("Enter the color of the banana (green, yellow, brown): ").strip().lower()
    if color == "green":
        print("The banana is unripe.")
    elif color == "yellow":
        print("The banana is ripe.")
    elif color == "brown":
        print("The banana is overripe.")
    else:
        print("Unknown color for banana.")
elif fruit == "apple":
    color = input("Enter the color of the apple (green, red, yellow): ").strip().lower()
    if color == "green":
        print("The apple is unripe.")
    elif color == "red" or color == "yellow":
        print("The apple is ripe.")
    else:
        print("Unknown color for apple.")
else:
    print("Unknown fruit.")