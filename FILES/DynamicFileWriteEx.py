#Program to read the data from the Keyboard and write to the file
#DynamicFileWriteEx.py
import sys
with open("hyd.data","w") as fp:
	print("Enter the lines of text and press 'quit' to stop")
	while(True):
		kbdata=input()
		if(kbdata=="quit"):
			sys.exit()
		else:
			fp.write(kbdata+"\n")
	print("\nData written to the file--verify")
	