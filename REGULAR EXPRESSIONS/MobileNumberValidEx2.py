#Program for Validating Mobile Number
#MobileNumberValidEx2.py
import re
while(True):
	num=input("Enter a Mobile Number: ")
	if len(num)==10:
		res=re.search("[98]\d{8}",num)
		if res!=None:
			print("\t{} is valid Mobile Number".format(num))
			break
		else:
			print("\t{} is invalid Mobile Number because it contains Non-Digits/Non-Series".format(num))
	else:
		print("\t{} is Invalid Mobile Number---due to its invalid length---try again".format(num))