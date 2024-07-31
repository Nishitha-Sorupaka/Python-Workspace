#This program writes address of different people in addr.info file
#FileWriteEx1.py
with open("addr.info","w") as wp:
	#Write the address of Rossum
	wp.write("Guido Van Rossum\n")
	wp.write("3-4 Red Sea Side\n")
	wp.write("Python Software Foundation\n")
	wp.write("Netherlands")
	print("\nAddress Written to the file successfully")