#8. Property Decorators
#Problem:
#Use a property decorator in the Car class
#to make the model attribute read-only.

class Car:

    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model     # Store the model internally.

    # Property decorator
    # Allows us to read the model like an attribute.
    @property
    def model(self):
        return self._model


# Take input from the user.
brand = input("Enter car brand: ")
model = input("Enter car model: ")

# Create an object.
car1 = Car(brand, model)

# Print the details.
print("\nCar Details")
print("Brand:", car1.brand)
print("Model:", car1.model)