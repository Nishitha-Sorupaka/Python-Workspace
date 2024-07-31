#program for extracting the mail from file(empmails.data) by using RegExpr
#ExtractMailsEx1.py
import re
try:
	with open("D:\\Python-Workspace\\REGULAR EXPRESSIONS\\Files\\empmails.data","r") as fp:
		filedata=fp.read()
		names=re.findall("[A-Z][a-z]+",filedata)
		mails=re.findall("[A-Za-z0-9._]+[@][A-Za-z0-9.]+",filedata)
		print("-"*50)
		for name,mail in zip(names,mails):
			print("\t{}---{}".format(name,mail))
		print("-"*50)
except FileNotFoundError:
	print("File Does not Exist")