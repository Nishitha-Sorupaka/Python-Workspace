#Program for searching all except lower Case Alphabets
#RegExp10.py
import re
mattab=re.finditer('[^a-z]',"cAK@2aLp4#Gq8HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp10.py
--------------------------------------------------
Start Index: 1 End Index: 2 Value: A
Start Index: 2 End Index: 3 Value: K
Start Index: 3 End Index: 4 Value: @
Start Index: 4 End Index: 5 Value: 2
Start Index: 6 End Index: 7 Value: L
Start Index: 8 End Index: 9 Value: 4
Start Index: 9 End Index: 10 Value: #
Start Index: 10 End Index: 11 Value: G
Start Index: 12 End Index: 13 Value: 8
Start Index: 13 End Index: 14 Value: H
Start Index: 15 End Index: 16 Value: Q
--------------------------------------------------
'''