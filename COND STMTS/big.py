#Wap which will accept two numerical integer values and decide the biggest among them and equality of the numbers?
#big.py

n1=float(input("Enter Number1:"))
n2=float(input("Enter a Number2:"))
if(n1==n2):
	print("Both the values are equal")
else:
	if(n1>n2):
		print("Biggest = {}".format(n1))
	else:
		print("Biggest = {}".format(n2))