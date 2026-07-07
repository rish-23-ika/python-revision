#7. Static Method
#Problem:
#Add a static method to the Car class
#that returns a general description of a car.


class Car:

    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Static method
    # It belongs to the class, not to any object.
    @staticmethod
    def description():
        return "A car is a four-wheeled vehicle used for transportation."


# Take input from the user.
brand = input("Enter car brand: ")
model = input("Enter car model: ")

# Create an object.
car1 = Car(brand, model)

# Call the static method.
print("\nDescription:")
print(Car.description())