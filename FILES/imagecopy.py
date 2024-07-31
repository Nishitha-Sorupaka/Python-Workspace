#This program copy an image by using files
#imagecopy.py
with open("C:\\Users\\nishi\\OneDrive\\Desktop\\cat.jpg","rb") as fp:
	filedata=fp.read()
	with open("cat.png","wb") as wp:
		wp.write(filedata)
		print("Image copied---verify")