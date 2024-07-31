#Program for searching All Alphabets(Upper & Lower)
#RegExp15.py
import re
mattab=re.finditer('[a-zA-Z]',"!cAK@2aLp4#Gq8HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp15.py
--------------------------------------------------
Start Index: 1 End Index: 2 Value: c
Start Index: 2 End Index: 3 Value: A
Start Index: 3 End Index: 4 Value: K
Start Index: 6 End Index: 7 Value: a
Start Index: 7 End Index: 8 Value: L
Start Index: 8 End Index: 9 Value: p
Start Index: 11 End Index: 12 Value: G
Start Index: 12 End Index: 13 Value: q
Start Index: 14 End Index: 15 Value: H
Start Index: 15 End Index: 16 Value: b
Start Index: 16 End Index: 17 Value: Q
Start Index: 17 End Index: 18 Value: w
--------------------------------------------------
'''