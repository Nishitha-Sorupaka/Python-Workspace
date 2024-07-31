#Program for Extracting Student names and Marks where in the information present in File(student.data). by using Regular Expression.
#ExtractStudNamesMarksFilesEx1.py
import re
try:
	with open("D:\\Python-Workspace\\REGULAR EXPRESSIONS\\Files\\studdents.data","r") as fp:
		filedata=fp.read()
		names=re.findall("[A-Z][a-z]+",filedata)
		marks=re.findall("\d{2}",filedata)
		print("-"*50)
		for name,mark in zip(names,marks):
			print("\t{}---{}".format(name,mark))
		print("-"*50)
except FileNotFoundError:
	print("File Does not Exist")