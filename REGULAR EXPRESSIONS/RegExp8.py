#Program for searching all Except Upper Case Alphabets
#RegExp8.py
import re
mattab=re.finditer('[^A-Z]',"cAK@2aLp4#Gq8HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp8.py
--------------------------------------------------
Start Index: 0 End Index: 1 Value: c
Start Index: 3 End Index: 4 Value: @
Start Index: 4 End Index: 5 Value: 2
Start Index: 5 End Index: 6 Value: a
Start Index: 7 End Index: 8 Value: p
Start Index: 8 End Index: 9 Value: 4
Start Index: 9 End Index: 10 Value: #
Start Index: 11 End Index: 12 Value: q
Start Index: 12 End Index: 13 Value: 8
Start Index: 14 End Index: 15 Value: b
Start Index: 16 End Index: 17 Value: w
--------------------------------------------------
'''