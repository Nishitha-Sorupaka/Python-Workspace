#area.py
'''
Area of Circle = PI*r**2
Area of Rectangle = l*b
Area of Square = s**2
Area of Triangle = 1\2 * b*h

'''

def circle():
	PI=3.14
	r=int(input("Enter Radius: "))
	print("Area of Circle = {}".format(PI*(r**2)))


def rectangle():
	l=int(input("Enter Length of the Rectangle:"))
	b=int(input("Enter Breadth of the Rectangle:"))
	print("Area of Rectangle = {}".format(l*b))

def square():
	s=int(input("Enter the side of a Square:"))
	print("Area of Square = {}".format(s**2))

def triangle():
	b=int(input("Enter Breadth of the Triangle:"))
	h=int(input("Enter Height of the Triangle:"))
	print("Area of Triangle = {}".format(0.5*b*h))

