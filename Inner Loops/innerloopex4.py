#innerloopex4.py
for i in range(1,6):
	print("-"*50)
	print("Value of i={}".format(i))
	print("-"*50)
	j=1
	while j<4:
		print("\tValue of j={}".format(j))
		j=j+1
	else:
		print("-"*50)
		print("Out of Inner while Loop")

else:
	print("-"*50)
	print("Out of Outer for loop")
	print("-"*50)