#Reading Employee Details using unpickling 
#empunpick.py
import pickle
try:
	with open("emp.data","rb") as fp:
		print("-"*50)
		print("Employee Records")
		print("-"*50)
		while(True):
			try:
				obj=pickle.load(fp)
				for val in obj:
					print("{}".format(val),end=" ")
				print()
			except EOFError:
				print("-"*50)
				break
except FileNotFoundError:
	print("File Does not Exist !")
