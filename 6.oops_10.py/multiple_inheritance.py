#10. Multiple Inheritance
#Problem:
#Create two classes Battery and Engine.
#Let the ElectricCar class inherit from both.


# First parent class
class Battery:

    def battery_info(self):
        print("Battery: 75 kWh")


# Second parent class
class Engine:

    def engine_info(self):
        print("Engine: Electric Motor")


# Child class inherits from both Battery and Engine.
class ElectricCar(Battery, Engine):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# Take input from the user.
brand = input("Enter car brand: ")
model = input("Enter car model: ")

# Create an object.
car1 = ElectricCar(brand, model)

# Print details.
print("\nCar Details")
print("Brand:", car1.brand)
print("Model:", car1.model)

# Call methods from both parent classes.
car1.battery_info()
car1.engine_info()