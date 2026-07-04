object types / data types

-Numbers: 
        integers (1, 2, 3), 
        decimal floating-points (3.14), 
        complex numbers (3 + 4j) 
        0b111
        decimal()
        fraction()
        
-strings:
        'spam'
        "spam"
        "bob's"
        b'a\x01c'

list:
        uses square brackets [1, 2, 3],
         holds a collection of ordered items 
         starting at index 0, 
         and is highly mutable 
         (you can add, change, or remove items)
    list = [1,3,4,[2,'three'],5]

tuple:
        Similar to lists but written with parentheses (1, 2, 3) 
        They are ordered, 
        immutable—once created, you can't alter their content.
    (1,'spam' ,2 , 3, 'A')

dictionary:
        Instead of using numbers (0, 1, 2) as indexes, 
        dictionaries store data in Key-Value pairs inside curly braces {} 
        You give each piece of data a custom name (a key), 
        like {"comic": "Nagraj"} 
        If you try to call a key that doesn't exist, Python will trigger a KeyError

set:
        ('abc') 
        ('a','b','c')

file mechanism:
        python can easily work with fiiles, excel, pdfs
        by importing modules 
        open('world.txt')

Booleans: 
        Simply True or False

None: 
        A special type used to represent an empty
        None

-functions, modules, classes

-advanced types:
    decorators, genearators, iterators
metaProgramming

modules like
    math
    random

len(): Tells you the size/length of strings, lists, or dictionaries using human-readable counts (not starting from zero)
-1 case

dir(): If you pass an object into dir(), Python will print out every single method and operation available for that data type

