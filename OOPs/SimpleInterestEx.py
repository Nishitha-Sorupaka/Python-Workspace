#Program for calculating Simple Interest using Classes and Methods
#SimpleInterestEx.py
class SimpleInterest:pass

#main program
s=SimpleInterest() #here si is the object
print("Content of s= ",s.__dict__)
print("--------------------------------")
s.p=float(input("Enter Principle Amount:"))
s.t=float(input("Enter Time:"))
s.r=float(input("Enter Rate of Interest:"))
#cal si and totamt
s.si=(s.p*s.t*s.r)/100
s.totamt=s.p+s.si
#display the values
print("==================================")
print("\tR E S U L T S")
print("==================================")
print("Principle Amount={}".format(s.p))
print("Time ={}".format(s.t))
print("Rate of Interest={}".format(s.r))
print("---------------------------------")
print("Simple Interest={}".format(s.si))
print("Total Amount to Pay={}".format(s.totamt))
print("==================================")