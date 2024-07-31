#kwdparamex2.py
def dispstuddet(sno,sname,marks,crs="PYTHON"):
	print("{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#main Program

print("-"*50)
print("Stno\tName\tMarks\tCourse")
print("-"*50)
dispstuddet(100,"RS",66.66)
dispstuddet(101,"JG",16.55)
dispstuddet(marks=33.33,sno=102,sname="RT")
dispstuddet(103,marks=10.11,sname="MC")
dispstuddet(marks=13.33,crs="JAVA",sno=104,sname="ZC")
print("-"*50)