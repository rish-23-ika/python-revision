#9. Class Inheritance and isinstance() Function
#Problem:
#Demonstrate the use of isinstance() to check if
#my_tesla is an instance of Car and ElectricCar.


# Parent class
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# Child class
class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


# Take input from the user.
brand = input("Enter car brand: ")
model = input("Enter car model: ")
battery = input("Enter battery size: ")

# Create an ElectricCar object.
my_tesla = ElectricCar(brand, model, battery)

# Check the object's type.
print("\nIs my_tesla a Car?", isinstance(my_tesla, Car))
print("Is my_tesla an ElectricCar?", isinstance(my_tesla, ElectricCar))