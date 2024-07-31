#Program for searching for all except Digits
#RegExp22.py
import re
mattab=re.finditer('[\D]',"!c AK@2a Lp4#Gq8 HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp22.py
--------------------------------------------------
Start Index: 0 End Index: 1 Value: !
Start Index: 1 End Index: 2 Value: c
Start Index: 2 End Index: 3 Value:
Start Index: 3 End Index: 4 Value: A
Start Index: 4 End Index: 5 Value: K
Start Index: 5 End Index: 6 Value: @
Start Index: 7 End Index: 8 Value: a
Start Index: 8 End Index: 9 Value:
Start Index: 9 End Index: 10 Value: L
Start Index: 10 End Index: 11 Value: p
Start Index: 12 End Index: 13 Value: #
Start Index: 13 End Index: 14 Value: G
Start Index: 14 End Index: 15 Value: q
Start Index: 16 End Index: 17 Value:
Start Index: 17 End Index: 18 Value: H
Start Index: 18 End Index: 19 Value: b
Start Index: 19 End Index: 20 Value: Q
Start Index: 20 End Index: 21 Value: w
--------------------------------------------------
'''