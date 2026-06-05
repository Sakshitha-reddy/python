tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter the number: "))
i=0
while i<len(tup):
    if(tup[i]==x):
        print("number is present in the tuple")
        break
        i+=1