#digitsum1.py
n=int(input("Enter any Number:"))
if(n<=0):
	print('Invalid input')
else:
	convert=str(n)
	s=0
	for x in convert:
		rev=int(x)
		s=s+rev
	else:
		print("Sum= {}".format(s))