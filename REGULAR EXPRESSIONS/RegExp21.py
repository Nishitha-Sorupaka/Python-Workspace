#Program for searching for Digits
#RegExp21.py
import re
mattab=re.finditer('[\d]',"!c AK@2a Lp4#Gq8 HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp21.py
--------------------------------------------------
Start Index: 6 End Index: 7 Value: 2
Start Index: 11 End Index: 12 Value: 4
Start Index: 15 End Index: 16 Value: 8
--------------------------------------------------

'''