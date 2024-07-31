#Program reads the data from file and displays on console---read()
#FileReadEx1.py
try:
	filename=input("Enter any file name:")
	with open(filename) as fp:
		filedata=fp.read()
		print("Type of filedata",type(filedata))
		print("-"*50)
		print("Content of the File:")
		print("-"*50)
		print(filedata)
		print("-"*50)
except FileNotFoundError:
	print(" '{}' File Does not exist !".format(filename))