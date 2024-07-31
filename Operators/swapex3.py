#Operators
#swapex3.py
#This program is used to swap two values using Bitwise XOR operator
a=int(input("Enter Value of a:"))
b=int(input("Enter Value of b:"))
#Original Values
print("Original Value of a ={}".format(a))
print("Original Value of b ={}".format(b))
#Swapping
a=a^b
b=a^b
a=a^b
#Swapped Values
print("Swapped Value of a ={}".format(a))
print("Swapped Value of b ={}".format(b))