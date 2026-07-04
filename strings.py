
#understand slicing
num_list = [0,1,2,3,4,5,6,7,8,9]
print(num_list[2:5])  ##slicing the list from index 2 to index 4 (5 is exclusive)
print(num_list[:5])   ##slicing the list from the beginning to index 4 (5 is exclusive)
print(num_list[5:])   ##slicing the list from index 5 to the end of the list
print(num_list[:])    ##slicing the entire list 

print(num_list[1:8:2])  ##slicing the list from index 1 to index 7 (8 is exclusive) with a step of 2, it will select every second element in the specified range. So it will select the elements at index 1, 3, 5, and 7 from the num_list.


chai = "lemon chai"
print(chai)  
print (chai[0]) 
print (chai[1])

slice_chai = chai[2:6]
print(slice_chai)   ##slicing the string from index 0 to index 5 (6 is exclusive)


print(chai.lower())
print(chai.upper())

A = "   masala chai   "
print(A.strip())  ##removes the leading and trailing whitespace from the string A
A = "masala chai"
print(A.replace("masala", "lemon"))  ##replaces the substring "masala" with "lemon" in the string A

CHAI = "lemon, GINGER, cardamom, cinnamon"
print(CHAI.split(", "))  ##splits the string CHAI into a list of substrings using ", " as the delimiter. The resulting list will contain the substrings "lemon", "GINGER", "cardamom", and "cinnamon".


B = "RISHIKA IS VERY VERY SWEET GIRL"
print(B.find("SWEET"))  ##finds the index of the first occurrence of the substring "SWEET" in the string B. If the substring is found, it returns the index; otherwise, it returns -1. In this case, it will return 10, which is the index of the first character of the substring "SWEET" in the string B.
print(B.count("VERY"))  ##counts the number of occurrences of the substring "VERY" in the string B. In this case, it will return 2, as the substring "VERY" appears twice in the string B.

chai_type = "masala"
quantity = 2
order = "I want to drink {} cups of {} chai."
print(order.format(quantity, chai_type))


chai_variety = ["lemon", "ginger", "cardamom", "cinnamon"]
print(" ".join(chai_variety))
print("-".join(chai_variety))

print(len(chai))

for letter in chai:   ##iterating through each character in the string chai and printing it
    print(letter)


#cases
chai = "he said, \"masala chai is good\"."
print(chai)  ##the backslash \ is used to escape the double quotes within the string, allowing us to include the double quotes as part of the string without causing a syntax error. When we print the string, it will display as: he said, "masala chai is good".

chai = "Masala\nChai"
print(chai)

chai = r"masala\nchai"
print(chai)

chai = "masala chai"
print("masala" in chai)

print("masalaa" in chai)




