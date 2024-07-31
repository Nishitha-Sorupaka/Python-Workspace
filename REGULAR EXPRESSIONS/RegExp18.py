#Program for searching for All except Space Character
#RegExp18.py
import re
mattab=re.finditer('[\S]',"!c AK@2a Lp4#Gq8 HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''
--------------------------------------------------
Start Index: 0 End Index: 1 Value: !
Start Index: 1 End Index: 2 Value: c
Start Index: 3 End Index: 4 Value: A
Start Index: 4 End Index: 5 Value: K
Start Index: 5 End Index: 6 Value: @
Start Index: 6 End Index: 7 Value: 2
Start Index: 7 End Index: 8 Value: a
Start Index: 9 End Index: 10 Value: L
Start Index: 10 End Index: 11 Value: p
Start Index: 11 End Index: 12 Value: 4
Start Index: 12 End Index: 13 Value: #
Start Index: 13 End Index: 14 Value: G
Start Index: 14 End Index: 15 Value: q
Start Index: 15 End Index: 16 Value: 8
Start Index: 17 End Index: 18 Value: H
Start Index: 18 End Index: 19 Value: b
Start Index: 19 End Index: 20 Value: Q
Start Index: 20 End Index: 21 Value: w
--------------------------------------------------
'''