#ServerResultDataBaseEx1.py
import socket
import mysql.connector
s=socket.socket()
s.bind(("localhost",8558))
s.listen(2)
print("SSP is ready to Accept any CSP Request")
while(True):
	try:
		csock,caddr=s.accept()
		stno=int(csock.recv(1024).decode())
		#PDBC Code
		con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="batch6pm")
		cur=con.cursor()
		cur.execute("select * from result where sno = %d" %stno)
		record=cur.fetchone()
		if(record==None):
			csock.send(("{} Number does not exist".format(str(stno))).encode())
		else:
			s1="Student Number="+str(record[0])
			s2="Student Name="+str(record[1])
			s3="Student Marks in C="+str(record[2])
			s4="Student Marks in C++="+str(record[3])
			s5="Student Marks in PYTHON="+str(record[4])
			s6="Student Total Marks="+str(record[5])
			s7="Student Percentage of Marks="+str(record[6])
			s8="Student Grade="+str(record[7])
			res=s1+"\n"+s2+"\n"+s3+"\n"+s4+"\n"+s5+"\n"+s6+"\n"+s7+"\n"+s8
			csock.send(res.encode())
	except ValueError:
		csock.send("Don't Enter alnums,strs and symbols for student Number".encode())
	except mysql.connector.DatabaseError as db:
		csock.send(("Problem in MySQL DB:"+db).encode())
	except :
		csock.send("Ooops Some thing went wrong".encode())



