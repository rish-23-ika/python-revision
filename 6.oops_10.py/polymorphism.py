#5. Polymorphism
#Problem:
#Demonstrate polymorphism by defining a method fuel_type
#in both Car and ElectricCar classes, but with different behaviors.

# Parent class
class Car:

    def fuel_type(self):
        print("Fuel Type: Petrol or Diesel")

# Child class
class ElectricCar(Car):

    # Same method name as the parent class
    # but with a different implementation.
    def fuel_type(self):
        print("Fuel Type: Electric Battery")

# Create objects.
car1 = Car()
car2 = ElectricCar()

# Call the same method.
car1.fuel_type()
car2.fuel_type()