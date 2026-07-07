#3. Inheritance
#Problem:
#Create an ElectricCar class that inherits from the Car class
#and has an additional attribute battery_size.


# Parent class
class Car:

    # Constructor of Car class
    def __init__(self, brand, model):
        self.brand = brand          # Store the brand.
        self.model = model          # Store the model.

# Child class
# ElectricCar inherits all the properties of Car.
class ElectricCar(Car):

    # Constructor of ElectricCar class
    def __init__(self, brand, model, battery_size):

        # Call the constructor of the parent class.
        super().__init__(brand, model)

        # New attribute of ElectricCar.
        self.battery_size = battery_size


# Take input from the user.
brand = input("Enter car brand: ")
model = input("Enter car model: ")
battery = input("Enter battery size: ")

# Create an object.
car1 = ElectricCar(brand, model, battery)

# Print the details.
print("\nElectric Car Details")
print("Brand:", car1.brand)
print("Model:", car1.model)
print("Battery Size:", car1.battery_size)