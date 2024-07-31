#FileOpenEx5.py
with open("stud.info","w") as fp:
	print("File opened in Write mode Successfully !")
	print("Type of fp=",type(fp))
	print("="*50)
	print("File Name=",fp.name) #Gives name of the file
	print("File Mode=",fp.mode) #Gives File Opening Mode-x
	print("Is stud.info readable?",fp.readable()) # False
	print("Is stud.info writable?",fp.writable()) # True
	print("Is File closed?",fp.closed) # False
	print("="*50)
#out of indentation of "with open() as"
print("\nIs file closed after indentation of with open()?=",fp.closed) # True