# Python Revision

Revising Python fundamentals and documenting concepts with examples.

Topics covered:
- Hello World
- Data Types
- Numbers
- Strings
- Lists
- Dictionaries
- condionals 10 practice questions
- loops 10 practice questions
- iteration tools
- functions 10 practice problems
- oops 10 practice questions

📚 OOP in Python - Quick Revision Notes
1. Basic Class and Object
Quick Revision
class → Blueprint for creating objects.
object → Instance of a class.
__init__() → Constructor, runs automatically when an object is created.
self → Refers to the current object.
Attributes store object data.
Interview Tip

A class is a blueprint, while an object is a real instance created from that blueprint.

2. Class Method and Self
Quick Revision
A method is a function inside a class.
Methods use self to access object data.
Call methods using:
object.method()
Interview Tip

self always refers to the current object and is automatically passed by Python when calling an instance method.

3. Inheritance
Quick Revision
Child class inherits properties and methods of the parent class.
Syntax:
class Child(Parent):
super() calls the parent constructor.
Interview Tip

Inheritance promotes code reusability by allowing child classes to reuse parent class functionality.

4. Encapsulation
Quick Revision
Hide internal data using private variables.
self.__brand
Access private data using getter methods.
Interview Tip

Encapsulation protects data by restricting direct access and providing controlled access through methods.

5. Polymorphism
Quick Revision
Same method name.
Different behavior.
Achieved through method overriding.
Interview Tip

Polymorphism means "One interface, many forms." The same method behaves differently for different objects.

6. Class Variables
Quick Revision
Shared by every object.
Declared outside __init__().
class Car:
    total_cars = 0
Interview Tip

Use class variables when the data should be common to all objects.

7. Static Method
Quick Revision
Doesn't use self.
Doesn't use cls.
Belongs to the class.
@staticmethod
Interview Tip

Static methods are utility functions related to a class but independent of object data.

8. Property Decorators
Quick Revision
@property creates a read-only attribute.
Access like a variable.
car.model

instead of

car.model()
Interview Tip

Use @property when you want controlled, read-only access to object data.

9. isinstance()
Quick Revision
isinstance(object, Class)

Returns

True
False

Checks whether an object belongs to a class (or its parent class).

Interview Tip

isinstance() is safer than comparing types because it also works with inheritance.

10. Multiple Inheritance
Quick Revision
class ElectricCar(Battery, Engine):

One child inherits from multiple parent classes.

Interview Tip

Multiple inheritance allows a child class to reuse functionality from more than one parent class.

🎯 Frequently Asked Interview Questions
What is OOP?

OOP (Object-Oriented Programming) is a programming paradigm based on objects and classes.

Four Pillars of OOP
Encapsulation
Inheritance
Polymorphism
Abstraction
Difference between Class and Object
Class	Object
Blueprint	Real instance
Logical entity	Physical entity
Defines attributes & methods	Stores actual values
What is a Constructor?

A special method

__init__()

that automatically runs whenever an object is created.

What is self?

self refers to the current object of a class.

What is Inheritance?

Allows one class to acquire properties and methods of another class.

What is Encapsulation?

Wrapping data and methods together while hiding internal implementation.

What is Polymorphism?

One method name having multiple implementations.

What is Method Overriding?

When a child class defines a method with the same name as the parent class.

Difference between Instance Variable and Class Variable
Instance Variable	Class Variable
Unique for every object	Shared by all objects
Defined using self	Defined inside class
Difference between Instance Method, Class Method and Static Method
Instance Method	Class Method	Static Method
Uses self	Uses cls	Uses neither
Works with object data	Works with class data	General utility function
What is @property?

Allows a method to behave like a read-only attribute.

What is super()?

Calls the constructor or methods of the parent class.

What is isinstance()?

Checks whether an object belongs to a class or any of its parent classes.

What is Multiple Inheritance?

A child class inherits from two or more parent classes.

📝 One-Line Revision
Class → Blueprint
Object → Instance of a class
Constructor → __init__()
self → Current object
Method → Function inside a class
Inheritance → Reuse parent class
Encapsulation → Hide data
Polymorphism → Same method, different behavior
Class Variable → Shared by all objects
Static Method → No self, no cls
Property → Read-only attribute
isinstance() → Checks object type
Multiple Inheritance → One child, multiple parents


More topics will be added as I continue revising Python.
