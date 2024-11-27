set1 = {'a','b','c',2}
set2 = {'d','e','f'}
set3 = {1, 2, 3}
mySets = set1.union(set2)
print(mySets)

mySets2= set1 | set2 # ulta palta join kore
print(mySets2) 

mySets3 = set1.union(set2,set3)
print(mySets3)

mySetMil = set1.intersection(set3) # ja mil thake take dakhabe
print(mySetMil)

mySet4 = set1.difference(set2) # set1 a ja ja omil tai dakhabe
print(mySet4)



