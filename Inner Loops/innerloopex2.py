#innerloopex2.py
i=1
while i<6:
	print("-"*50)
	print("Value of i={}".format(i))
	print("-"*50)
	j=1
	while j<4:
		print("\tValue of j={}".format(j))
		j=j+1
	else:
		print("-"*50)
		print("Out of inner while loop")
		print("-"*50)
	i=i+1
else:
	print("-"*50)
	print("Out of Outer while loop")
	print("-"*50)
	