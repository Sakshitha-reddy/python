name=input("enter your name:")
print(type(name))
print(name)#by default input function converts everthing into a string data type ,it converts 2 int to string,2.5 float to string etc

#so to specify a particular data type we need to declare it in the beginning itself ex:int(input())

val=int(input("enter your val:"))
print(type(val))
print(val)

val=float(input("enter your val:"))
print(type(val))
print(val)