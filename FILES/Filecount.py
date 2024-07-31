#This program counts the number of lines, words and chars in a file
#Filecount.py
filename=input("Enter a File Name: ")
try:
	with open(filename,"r") as fp:
		print("-"*50)
		print("Content of the File: ")
		print("-"*50)
		for kvr in fp:
			print(kvr)
		else:
			print("-"*50)
			nl=0
			nw=0
			nc=0
			fp.seek(0)
			lines=fp.readlines()
			for line in lines:
				nl=nl+1
				nw=nw+len(line.split())
				nc=nc+len(line)
			else:
				print("Number of Lines: {}".format(nl))
				print("Number of Words: {}".format(nw))
				print("Number of Characters: {}".format(nc))
except FileNotFoundError:
	print("File Does not Exist !")