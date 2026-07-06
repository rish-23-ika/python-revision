#4. Function Returning Multiple Values
#Problem:
#Create a function that returns both the area and circumference of a circle given its radius.

def circle(radius):
    pi=3.14
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference
radius = float(input("Enter the radius of the circle: "))
area, circumference = circle(radius)
print(f"Area: {area}, Circumference: {circumference}")
