#SquaresCubesOOP1.py
class SquareCube:
	lst=list()


	def addNumToList(self):
		n=int(input("Enter How many Numbers you want to add in a List: "))
		if(n<=0):
			print("{} is invalid input".format(n))
		else:
			#self.lst=list()
			for i in range(1,n+1):
				while(True):
					num=input("Enter {} Number: ".format(i))
					if(int(num)>=0):
						break
					else:
						print("Invalid input. Please enter a non-negative number.")
				self.lst.append(num)
		print(self.lst)

	
	@classmethod
	def squarescubes(cls):
		nsum,sqsum,csum,nmul,sqmul,cmul=0,0,0,1,1,1
		print("-"*50)
		print("\tNumber:\tSquare\tCube")
		print("-"*50)
		for i in range(0,len(cls.lst)):
			print("\t{}\t{}\t{}".format(int(cls.lst[i]),int(cls.lst[i])**2,int(cls.lst[i])**3))
			nsum=nsum+int(cls.lst[i])
			sqsum=sqsum+int(cls.lst[i])**2
			csum=csum+int(cls.lst[i])**3
			nmul=nmul*int(cls.lst[i])
			sqmul=sqmul*int(cls.lst[i])**2
			cmul=cmul*int(cls.lst[i])**3
		print("-"*50)
		print("Sum:\t{}\t{}\t{}".format(nsum,sqsum,csum))
		print("-"*50)
		print("Mul:\t{}\t{}\t{}".format(nmul,sqmul,cmul))
		print("-"*50)


#main program
obj=SquareCube()
obj.addNumToList()
SquareCube.squarescubes()