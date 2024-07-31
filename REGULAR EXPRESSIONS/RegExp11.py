#Program for searching all Digits
#RegExp11.py
import re
mattab=re.finditer('[0-9]',"cAK@2aLp4#Gq8HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp11.py
--------------------------------------------------
Start Index: 4 End Index: 5 Value: 2
Start Index: 8 End Index: 9 Value: 4
Start Index: 12 End Index: 13 Value: 8
--------------------------------------------------
'''