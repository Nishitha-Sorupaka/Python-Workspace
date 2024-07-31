#anonymousfunex4.py

findbig = lambda x,y: x if x>y else y
findsmall = lambda k,v: k if k<v else v

#main program
a=int(input("Enter First Value:"))
b=int(input("Enter Second Value:"))
print("max({},{})={}".format(a,b,findbig(a,b)))
print("min({},{})={}".format(a,b,findsmall(a,b)))