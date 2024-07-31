#Program for searching for Space Character
#RegExp17.py
import re
mattab=re.finditer('[\s]',"!c AK@2a Lp4#Gq8 HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp17.py
--------------------------------------------------
Start Index: 2 End Index: 3 Value:
Start Index: 8 End Index: 9 Value:
Start Index: 16 End Index: 17 Value:
--------------------------------------------------
'''