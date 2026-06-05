collection={1,2,3,4,5,"world"}
print(collection)
print(type(collection))

collection={1,2,2,2,2,3,4,5,5,5,"world","world"}#duplicate values are not allowed in sets,so set ignores them
print(collection)

empty_set={} #this creates an empty dictionary not an empty set
print(empty_set)    
print(type(empty_set))

empty_set=set() #to create an empty set we have to use set() function,{} is used to create an empty dictionary
print(empty_set)
print(type(empty_set))