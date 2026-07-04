import math

print (math.floor(4.7))  ##ROUNDS DOWN THE NUMBER TO THE NEAREST INTEGER
print (math.floor(4.2))
print (math.floor(-4.7))
print (math.floor(-4.3))   ##ROUNDS UP THE NUMBER TO THE NEAREST INTEGER

#floor takes to floor value 
#trunc takes to the integer part of the number, it just removes the decimal part without rounding.

print (math.trunc(4.7))
print (math.trunc(4.2))
print (math.trunc(-4.7))
print (math.trunc(-4.3))

print (99999999999999999999 * 2.1)

print (0o20) #octal 

print (0xFF) #hexadecimal

print (int ('64',8)) #converting octal to decimal
print (int ('64',16)) #converting hexadecimal to decimal
print (int ('10000',2)) #converting binary to decimal

#bitwise operators
print (5 & 3)  ##bitwise AND
print (5 | 3)  ##bitwise OR
print (5 ^ 3)  ##bitwise XOR
print (~5)     ##bitwise NOT
print (5 << 1) ##bitwise left shift
print (5 >> 1) ##bitwise right shift

import random
print (random.random()) ##generates a random float between 0.0 and 1.0  
print (random.randint(1,10)) ##generates a random integer between 1 and 10 (inclusive)

l1=[1,2,3,4,5]
print (random.choice(l1)) ##selects a random element from the list l1

print (random.shuffle(l1)) ##shuffles the elements of the list l1 in place
print (l1) ##prints the shuffled list l1