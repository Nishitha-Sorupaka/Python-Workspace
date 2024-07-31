#Program for generating 1 to N numbers where N is Positive(+ve)
#NumGenEx1.py
n=int(input("Enter how many Numbers you want to generate: ")) #n=10 -10   0
if(n<=0):
	print("{} is Invalid input ".format(n))
else:
	print("-------------------------")
	print("Numbers within:{} ".format(n))
	print("-------------------------")
	i=1 # initialization part
	while(i<=n): # condition part
		print("\t{}".format(i))
		i=i+1 # updation part
	else:
		print("-------------------------")
		print("I am from else block")
		print("-------------------------")