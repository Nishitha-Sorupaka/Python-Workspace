#Wap which will accept a numerical value and decide whether it is positive or negative or zero?
#posnegzero1.py
n=float(input("Enter a Number:"))
if(n>0):
	print("{} is a positive number".format(n))
else:
	if(n<0):
		print("{} is a negative number".format(n))
	else:
		print("{} is equal to zero".format(n))
