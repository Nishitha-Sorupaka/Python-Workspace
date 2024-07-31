#Factorial.py
n=int(input("Enter a Number you want to calculate its Factorial !: "))
if(n<=0):
	print("Invalid Input")
else:
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	print("Factorial of {}! = {}".format(n,fact))