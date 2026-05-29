age=int(input("enter your age"))
if(age>=18):
    print("you are eligible")
elif(0<=age<18):
    print("you are not eligible")
else:
    print("invalid input")

    
grade=int(input("enter ur grade:"))
if(grade>=90):
    print("grade A")
elif(90>grade>=80):
    print("grade B")
elif(80>grade>=70):
    print("grade C")
elif(70>grade>=0):
    print("grade D")
else:
    print("invalid grade")