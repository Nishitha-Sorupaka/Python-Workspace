#This program writes iterable objects to the files---writelines()
#FileWriteEx2.py
d={10:"Python",20:"CPP",30:"Django"}
with open("stud.addr","a") as fp:
	fp.writelines(str(d)+"\n")
	print("\nIterable object data written to the file:")
	