#Program for searching all Alphabets Digits
#RegExp13.py
import re
mattab=re.finditer('[a-zA-Z0-9]',"cAK@2aLp4#Gq8HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''
--------------------------------------------------
Start Index: 0 End Index: 1 Value: c
Start Index: 1 End Index: 2 Value: A
Start Index: 2 End Index: 3 Value: K
Start Index: 4 End Index: 5 Value: 2
Start Index: 5 End Index: 6 Value: a
Start Index: 6 End Index: 7 Value: L
Start Index: 7 End Index: 8 Value: p
Start Index: 8 End Index: 9 Value: 4
Start Index: 10 End Index: 11 Value: G
Start Index: 11 End Index: 12 Value: q
Start Index: 12 End Index: 13 Value: 8
Start Index: 13 End Index: 14 Value: H
Start Index: 14 End Index: 15 Value: b
Start Index: 15 End Index: 16 Value: Q
Start Index: 16 End Index: 17 Value: w
--------------------------------------------------
'''