#FileOpenEx3.py
fp=open("hyd.data","a") # try w+ r+ a+
print("File created and opened in Write mode successfully !")
print("Type of fp=",type(fp))
print("="*50)
print("File Name=",fp.name) #Gives name of the file
print("File Mode=",fp.mode) #Gives File Opening Mode-a
print("Is stud.info readable?",fp.readable()) # False
print("Is stud.info writable?",fp.writable()) # True
print("Is File closed?",fp.closed) # False
print("="*50)