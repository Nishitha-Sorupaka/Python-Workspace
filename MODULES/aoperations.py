#Write a python program which will calculate all types of Arithmetic Operators by using Modules with Menu Driven Application
#aoperations.py

def addop():
	a=float(input("Enter First Value: "))
	b=float(input("Enter Second Value: "))
	print("Sum({},{})={}".format(a,b,a+b))

def subop():
	a=float(input("Enter First Value: "))
	b=float(input("Enter Second Value: "))
	print("Sub({},{})={}".format(a,b,a-b))

def mulop():
	a=float(input("Enter First Value: "))
	b=float(input("Enter Second Value: "))
	print("mul({},{})={}".format(a,b,a*b))

def divop():
	a=float(input("Enter First Value: "))
	b=float(input("Enter Second Value: "))
	print("Div({},{})={}".format(a,b,a/b))
	print("Floor Div({},{})={}".format(a,b,a//b))

def modop():
	a=float(input("Enter First Value: "))
	b=float(input("Enter Second Value: "))
	print("ModDiv({},{})={}".format(a,b,a%b))

def expoop():
	a=float(input("Enter Base Value: "))
	b=float(input("Enter Power Value: "))
	print("exp({},{})={}".format(a,b,a**b))



