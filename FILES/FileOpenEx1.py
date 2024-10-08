#FileOpenEx1.py
try:
	fp=open("stud.info","r")
	
except FileNotFoundError:
	print("File Does not exist !")
else:
	print("File opened in Read Mode Successfully")
	print("Type of fp=",type(fp))
	print("="*50)
	print("File Name=",fp.name) #Gives name of the file
	print("File Mode=",fp.mode) #Gives File Opening Mode-r
	print("Is stud.info readable?",fp.readable()) # True
	print("Is stud.info writable?",fp.writable()) # False
	print("Is File closed?",fp.closed) # False
	print("="*50)
finally:
	print("\nI am from Finally block")
	fp.close() #Manual closing of file
	print("Is File closed?",fp.closed) # True

