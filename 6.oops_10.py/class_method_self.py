#2. Class Method and Self
#Problem:
#Add a method to the Car class that displays the full name of the car (brand and model).

# Create a class named Car.
class Car:

    # Constructor
    # It runs automatically when an object is created.
    def __init__(self, brand, model):
        self.brand = brand      # Store the car's brand.
        self.model = model      # Store the car's model.

    # This is a class method.
    # 'self' refers to the current object.
    def full_name(self):
        print("Car:", self.brand, self.model)


# Take input from the user.
brand = input("Enter car brand: ")
model = input("Enter car model: ")

# Create an object.
car1 = Car(brand, model)

# Call the method using the object.
car1.full_name()