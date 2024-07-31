#Program for searching All except Alphabets
#RegExp16.py
import re
mattab=re.finditer('[^a-zA-Z]',"!cAK@2aLp4#Gq8HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''
--------------------------------------------------
Start Index: 0 End Index: 1 Value: !
Start Index: 4 End Index: 5 Value: @
Start Index: 5 End Index: 6 Value: 2
Start Index: 9 End Index: 10 Value: 4
Start Index: 10 End Index: 11 Value: #
Start Index: 13 End Index: 14 Value: 8
--------------------------------------------------
'''