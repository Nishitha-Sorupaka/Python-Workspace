#This program reads all lines from file---readlines()
#FileReadEx4.py
filename=input("Enter the file name:")
try:
	with open(filename,"r") as fp:
		line=fp.readlines()
		for line in line:
			print("{}".format(line),end="")
except FileNotFoundError:
	print("File does not exist !")
