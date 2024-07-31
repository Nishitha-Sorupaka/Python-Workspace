#Wap which will calculate Area and perimeter of Rectangle
#areaandperimeterofrectangle.py

#APPROACH-1
# INPUT from Function Calls
# PROCESSING done in Function Body
# RESULT gives to Function Call

def areaandperimeterofrectangle(length,breadth):
	area = length*breadth
	perimeter=2*(length+breadth)
	return area,perimeter

#Main Program - Approach-1
length=int(input("Enter Length of the Rectangle: "))
breadth=int(input("Enter Breadth of the Rectangle: "))
area=areaandperimeterofrectangle(length,breadth)
print("Area of Rectangle: {}".format(area[0]))
print("Perimeter of Rectangle: {}".format(area[1]))


#APPROACH-2
# INPUT taking in Function Body
# PROCESSING done in Function Body
# RESULT given in Function Body

def areaandperimeterofrectangle():
	length=int(input("Enter Length of the Rectangle: "))
	breadth=int(input("Enter Breadth of the Rectangle: "))
	area = length*breadth
	perimeter=2*(length+breadth)
	print("Area of Rectangle: {}".format(area))
	print("Perimeter of Rectangle: {}".format(perimeter))

#Main Program - Approach-2

areaandperimeterofrectangle()



#APPROACH-3
# INPUT taking in Function Calls
# PROCESSING done in Function Body
# RESULT given in Function Body

def areaandperimeterofrectangle(length,breadth):
	area = length*breadth
	perimeter=2*(length+breadth)
	print("Area of Rectangle: {}".format(area))
	print("Perimeter of Rectangle: {}".format(perimeter))

#Main Program - Approach-3
length=int(input("Enter Length of the Rectangle: "))
breadth=int(input("Enter Breadth of the Rectangle: "))
areaandperimeterofrectangle(length,breadth)



#APPROACH-4
# INPUT taken in Function Body
# PROCESSING done in Function Body
# RESULT gives to Function Call

def areaandperimeterofrectangle():
	length=int(input("Enter Length of the Rectangle: "))
	breadth=int(input("Enter Breadth of the Rectangle: "))
	area = length*breadth
	perimeter=2*(length+breadth)
	return length,breadth,area,perimeter

#Main Program - Approach-2

length,breadth,area,perimeter=areaandperimeterofrectangle()
print("Area of Rectangle = length: {} X breadth: {} = {}".format(length,breadth,area))
print("Perimeter of Rectangle = 2* (length: {} + breadth: {}) = {}".format(length,breadth,perimeter))
area = areaandperimeterofrectangle()
print("Area of Rectangle = length: {} X breadth: {} = {}".format(area[0],area[1],area[2]))
print("Perimeter of Rectangle = 2* (length: {} + breadth: {}) = {}".format(area[0],area[1],area[2],area[3]))


""" Approach-1 --------> Function with Parameters and with Return Type
	Approach-2 --------> Function without Parameters and without Return Type
    Approach-3 --------> Function with Parameters and without Return Type
    Approach-4 --------> Function without Parameters and with Return Type  """