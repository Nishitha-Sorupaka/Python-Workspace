#Program for displaying Multiplication table using for loop
#table1.py
n=int(input("Enter Which Number table you want to generate: ")) #n=10 -10   0
if(n<=0):
	print("{} is Invalid input ".format(n))
else:
	print("-------------------------")
	print("Multiplication table of {} ".format(n))
	print("-------------------------")
	for i in range(1,11):
		print("\t{} x {} = {}".format(n,i,n*i))
	else:
		print("\n-------------------------")
		print("Table Printed ")
		print("-------------------------")