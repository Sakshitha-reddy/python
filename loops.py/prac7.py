tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter the number: "))
for i in tup:
    if(i==x):
        print("x is present in the tuple")
        break
else:
       print("x is not present in the tuple")
    