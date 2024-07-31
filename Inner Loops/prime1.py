#prime1.py
lst=[2,3,5,7,9,11]
for n in lst:
			if(n<=1):
				print("{} is invalid input".format(n))
			else:
				print("-"*30)
				print("Number: {}".format(n))
				print("-"*30)
				res=False
				for i in range(2,n):
					if(n%i==0):
						res=True
						break
				if(res):
					print("{} is not a prime number".format(n))
				else:
					print("{} is a prime number".format(n))