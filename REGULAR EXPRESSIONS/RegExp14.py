#Program for searching Special Characters
#RegExp14.py
import re
mattab=re.finditer('[^a-zA-Z0-9]',"!cAK@2aLp4#Gq8HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp14.py
--------------------------------------------------
Start Index: 0 End Index: 1 Value: !
Start Index: 4 End Index: 5 Value: @
Start Index: 10 End Index: 11 Value: #
--------------------------------------------------
'''