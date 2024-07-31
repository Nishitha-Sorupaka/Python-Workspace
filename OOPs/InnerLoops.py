#InnerLoopsEx1.py
for i in range(1,6): #outer loop
    print("value of i outer loop : {}".format(i))
    print("-"*50)
    for j in range(1,4): #inner loop
        print("value of j inner loop : {}".format(j))
    else:
        print("\tI am coming from Inner loop")
        print("-" * 50)
else:
    print("\tI am coming from Outer loop")