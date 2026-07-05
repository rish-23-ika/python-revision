#6. Transportation Mode Selection
#Problem:
#Choose a mode of transportation based on the distance.

#Examples:
#- Distance < 3 km   → Walk
#- Distance 3–15 km  → Bike
#- Distance > 15 km  → Car

distance = int(input("Enter the distance in kilometers: "))

if distance < 3:
    mode = "Walking"
elif 3 <= distance <= 15:
    mode = "Bike"
elif distance > 15:
    mode = "Car"
else:
    mode = "fly"

print(f"The recommended mode of transportation is: {mode}")

