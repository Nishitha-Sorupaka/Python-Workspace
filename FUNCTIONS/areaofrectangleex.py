#Wap which will calculate area of Rectangle by using functions? 
#areaofrectangleex.py

#APPROACH-1
# INPUT from Function Calls
# PROCESSING done in Function Body
# RESULT gives to Function Call

def areaofrectangle(length,breadth):
	area = length*breadth
	return area

#Main Program - Approach-1
length=int(input("Enter Length of the Rectangle: "))
breadth=int(input("Enter Breadth of the Rectangle: "))
area=areaofrectangle(length,breadth)
print("Area of Rectangle: {}".format(area))


#APPROACH-2
# INPUT taking in Function Body
# PROCESSING done in Function Body
# RESULT given in Function Body

def areaofrectangle():
	length=int(input("Enter Length of the Rectangle: "))
	breadth=int(input("Enter Breadth of the Rectangle: "))
	area = length*breadth
	print("Area of Rectangle: {}".format(area))

#Main Program - Approach-2

areaofrectangle()



#APPROACH-3
# INPUT taking in Function Calls
# PROCESSING done in Function Body
# RESULT given in Function Body

def areaofrectangle(length,breadth):
	area = length*breadth
	print("Area of Rectangle: {}".format(area))

#Main Program - Approach-3
length=int(input("Enter Length of the Rectangle: "))
breadth=int(input("Enter Breadth of the Rectangle: "))
areaofrectangle(length,breadth)



#APPROACH-4
# INPUT taken in Function Body
# PROCESSING done in Function Body
# RESULT gives to Function Call

def areaofrectangle():
	length=int(input("Enter Length of the Rectangle: "))
	breadth=int(input("Enter Breadth of the Rectangle: "))
	area = length*breadth
	return length,breadth,area

#Main Program - Approach-2

length,breadth,area=areaofrectangle()
print("Area of Rectangle = length: {} X breadth: {} = {}".format(length,breadth,area))
area = areaofrectangle()
print("Area of Rectangle = length: {} X breadth: {} = {}".format(area[0],area[1],area[2]))


""" Approach-1 --------> Function with Parameters and with Return Type
	Approach-2 --------> Function without Parameters and without Return Type
    Approach-3 --------> Function with Parameters and without Return Type
    Approach-4 --------> Function without Parameters and with Return Type