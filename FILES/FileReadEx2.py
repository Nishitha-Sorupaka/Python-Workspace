#This program reads specific number of characters from file---read(no. of chars)
#FileReadEx2.py
with open("addr.info","r") as fp:
	print("Initial Index/Position of fp={}".format(fp.tell())) # 0
	filedata=fp.read(3)
	print("File Data=",filedata)
	print("Now Index/Position of fp={}".format(fp.tell()))
	filedata=fp.read(15)
	print("File Data=",filedata)
	print("Now Index/Position of fp={}".format(fp.tell()))
	filedata=fp.read()
	print("File Data=",filedata)
	print("Now Index/Position of fp={}".format(fp.tell()))
	fp.seek(0)
	filedata=fp.read()
	print("File Data=",filedata)
	print("Now Index/Position of fp={}".format(fp.tell()))