#4. Encapsulation
#Problem:
#Modify the Car class to encapsulate the brand attribute,
#making it private, and provide a getter method for it.

class Car:

    # Constructor
    def __init__(self, brand, model):
        self.__brand = brand      # Private attribute
        self.model = model        # Public attribute

    # Getter method
    # Used to access the private attribute.
    def get_brand(self):
        return self.__brand

# Take input from the user.
brand = input("Enter car brand: ")
model = input("Enter car model: ")

# Create an object.
car1 = Car(brand, model)

# Print the details.
print("\nCar Details")
print("Brand:", car1.get_brand())
print("Model:", car1.model)

