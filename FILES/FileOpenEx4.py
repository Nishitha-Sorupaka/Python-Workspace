#FileOpenEx4.py
try:
	fp=open("kvr.data","x") 
	print("File opened in Write mode Exclusively !")
	print("Type of fp=",type(fp))
	print("="*50)
	print("File Name=",fp.name) #Gives name of the file
	print("File Mode=",fp.mode) #Gives File Opening Mode-x
	print("Is stud.info readable?",fp.readable()) # False
	print("Is stud.info writable?",fp.writable()) # True
	print("Is File closed?",fp.closed) # False
	print("="*50)
except FileExistsError:
	print("File already exists !")