#Wap which will swap any type of values?
#swapvalue.py

#APPROACH-1
# INPUT from Function Calls
# PROCESSING done in Function Body
# RESULT gives to Function Call

def swap(value1,value2):
	value1,value2=value2,value1
	return value1,value2

#Main Program - Approach-1
value1=input("Enter Value-1: ")
value2=input("Enter Value-2: ")
print("Initial Values: {}, {}".format(value1,value2))
value1,value2=swap(value1,value2)
print("Swapped Values: {}, {}".format(value1,value2))


#APPROACH-2
# INPUT taking in Function Body
# PROCESSING done in Function Body
# RESULT given in Function Body

def swap():
	value1=input("Enter Value-1: ")
	value2=input("Enter Value-2: ")
	print("Initial Values: {}, {}".format(value1,value2))
	value1,value2=value2,value1
	print("Swapped Values: {}, {}".format(value1,value2))

#Main Program - Approach-2

swap()



#APPROACH-3
# INPUT taking in Function Calls
# PROCESSING done in Function Body
# RESULT given in Function Body

def swap(value1,value2):
	value1,value2=value2,value1
	print("Initial Values: {}, {}".format(value1,value2))
	value1,value2=value2,value1
	print("Swapped Values: {}, {}".format(value1,value2))

#Main Program - Approach-3
value1=input("Enter Value-1: ")
value2=input("Enter Value-2: ")
swap(value1,value2)



#APPROACH-4
# INPUT taken in Function Body
# PROCESSING done in Function Body
# RESULT gives to Function Call

def swap():
	value1=input("Enter Value-1: ")
	value2=input("Enter Value-2: ")
	print("Initial Values: {}, {}".format(value1,value2))
	value1,value2=value2,value1
	return value1,value2

#Main Program - Approach-2

value1,value2=swap()
print("Swapped Values: {}, {}".format(value1,value2))
value = swap()
print("Swapped Values: {}, {}".format(value[0],value[1]))



""" Approach-1 --------> Function with Parameters and with Return Type
	Approach-2 --------> Function without Parameters and without Return Type
    Approach-3 --------> Function with Parameters and without Return Type
    Approach-4 --------> Function without Parameters and with Return Type  """


