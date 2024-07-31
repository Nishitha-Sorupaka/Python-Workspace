#Program for searching for Special Symbols
#RegExp20.py
import re
mattab=re.finditer('[\W]',"!c AK@2a Lp4#Gq8 HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp20.py
--------------------------------------------------
Start Index: 0 End Index: 1 Value: !
Start Index: 2 End Index: 3 Value:
Start Index: 5 End Index: 6 Value: @
Start Index: 8 End Index: 9 Value:
Start Index: 12 End Index: 13 Value: #
Start Index: 16 End Index: 17 Value:
--------------------------------------------------
'''
