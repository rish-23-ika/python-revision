#1. Basic Class and Object
#Problem:
#Create a Car class with attributes like brand and model.
#Then create an instance of this class.

# 'class' is used to create a blueprint.
# Here we are creating a class named Car.
class Car:

    # __init__ is a constructor.
    # It runs automatically whenever a new object is created.
    # 'self' refers to the current object.
    # 'brand' and 'model' are parameters that receive values.
    def __init__(self, brand, model):
        self.brand = brand      # Store the brand in the object.
        self.model = model      # Store the model in the object.


# Take input from the user.
brand = input("Enter car brand: ")
model = input("Enter car model: ")

# Create an object (instance) of the Car class.
car1 = Car(brand, model)

# Access and print the object's attributes.
print("\nCar Details")
print("Brand:", car1.brand)
print("Model:", car1.model)