collection=set()
collection.add(1) #adding a single element to the set
collection.add(2)
collection.add(2)

collection.remove(1)#removing an element from the set
collection.clear() #removing all the elements from the set
print(collection) #duplicate values are not allowed in sets,so set ignores them

set1={1,2,3}
set2={3,4,5}
print(set1.union(set2)) #union of two sets
print(set1.intersection(set2)) #intersection of two sets