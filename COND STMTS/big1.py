#Wap which will accept three values and find the biggest among them?
#big1.py
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if((a>b)&(a>c)):
	print("{} is Bigger".format(a))
else:
	if((b>a)&(b>c)):
		print("{} is Bigger".format(b))
	else:
		print("{} is Bigger".format(c))
if((a==b)&(a==c)):
	print("All values are equal")