#Program for searching all lower Case Alphabets only
#RegExp9.py
import re
mattab=re.finditer('[a-z]',"cAK@2aLp4#Gq8HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp9.py
--------------------------------------------------
Start Index: 0 End Index: 1 Value: c
Start Index: 5 End Index: 6 Value: a
Start Index: 7 End Index: 8 Value: p
Start Index: 11 End Index: 12 Value: q
Start Index: 14 End Index: 15 Value: b
Start Index: 16 End Index: 17 Value: w
--------------------------------------------------
'''