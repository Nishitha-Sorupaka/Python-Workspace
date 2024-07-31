#innerloopex1.py
for i in range(1,6):
	print("-"*50)
	print("Value of i={}".format(i))
	print("-"*50)
	for j in range(1,4):
		print("\tValue of j={}".format(j))
	else:
		print("-"*50)
		print("Out of Inner for Loop")

else:
	print("-"*50)
	print("Out of Outer for loop")
	print("-"*50)