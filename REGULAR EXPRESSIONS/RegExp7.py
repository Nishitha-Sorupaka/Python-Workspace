#Program for searching all Upper Case Alphabets only
#RegExp7.py
import re
mattab=re.finditer('[A-Z]',"cAK@2aLp4#Gq8HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp7.py
--------------------------------------------------
Start Index: 1 End Index: 2 Value: A
Start Index: 2 End Index: 3 Value: K
Start Index: 6 End Index: 7 Value: L
Start Index: 10 End Index: 11 Value: G
Start Index: 13 End Index: 14 Value: H
Start Index: 15 End Index: 16 Value: Q
--------------------------------------------------
'''