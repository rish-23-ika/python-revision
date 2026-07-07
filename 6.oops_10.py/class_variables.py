#6. Class Variables
#Problem:
#Add a class variable to Car that keeps track
#of the number of cars created.


class Car:

    # Class variable
    # Shared by all objects.
    total_cars = 0

    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        # Increase the class variable whenever
        # a new object is created.
        Car.total_cars += 1


# Take input for first car.
brand1 = input("Enter first car brand: ")
model1 = input("Enter first car model: ")
car1 = Car(brand1, model1)

# Take input for second car.
brand2 = input("Enter second car brand: ")
model2 = input("Enter second car model: ")
car2 = Car(brand2, model2)

# Print total number of cars created.
print("\nTotal Cars Created:", Car.total_cars)