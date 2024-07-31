#This program calculates Square Root of a given Number
#squarerootex1.py

# INPUT from Function Calls
# PROCESSING done in Function Body
# RESULT gives to Function Call

#Function Definition
def squareroot(n):
	result=n**0.5
	return result



#main program

n=int(input("Enter a Number: "))
result=squareroot(n)
print("Square Root of {}= {}".format(n,result))