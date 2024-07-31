#anonymousfunex7.py

findbig = lambda l1: max(l1)
findsmall = lambda k: min(k)


#main program
lst=[10,20,-30,40,50,100,-4,-5,0,34,67]
print("max({})={}".format(lst,findbig(lst)))
print("min({})={}".format(lst,findsmall(lst)))