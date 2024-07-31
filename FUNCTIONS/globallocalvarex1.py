#globallocalvarex1.py

pfname="Rossum" #Global Variable
def learnDataSci():
	crs1="Data Science" #local Variable
	print("To develop '{}' based applications, we use '{}' lang\n invented by {}".format(crs1,lang,pfname))

def learnML():
	crs2="Machine Learning" #local Variable
	print("To develop '{}' based applications, we use '{}' lang\n invented by {}".format(crs2,lang,pfname))


def learnDL():
	crs3="Deep Learning" #local Variable
	print("To develop '{}' based applications, we use '{}' lang\n invented by {}".format(crs3,lang,pfname))


#main program
lang="PYTHON" #Global Variable
learnDataSci()
print("-"*50)
learnML()
print("-"*50)
learnDL()

