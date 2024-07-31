#FileOpenEx2.py
fp=open("stud.info","w")
print("File opened in Write mode successfully !")
print("Type of fp=",type(fp))
print("="*50)
print("File Name=",fp.name) #Gives name of the file
print("File Mode=",fp.mode) #Gives File Opening Mode-w
print("Is stud.info readable?",fp.readable()) # False
print("Is stud.info writable?",fp.writable()) # True
print("Is File closed?",fp.closed) # False
print("="*50)