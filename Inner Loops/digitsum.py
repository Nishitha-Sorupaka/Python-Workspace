#digitsum.py
n=int(input("Enter any Number:"))
if(n<=0):
	print('Invalid input')
else:
	s=0
	while(n>0):
		d=n%10
		s=s+d
		n=n//10
	else:
		print("Sum= {}".format(s))

		
