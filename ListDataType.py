list = ['ami','tumi','bhai','bon']
print(list[2])
list[2]='bon'
print(list)

# add items

# append method

# append always add item in the last of the list 

list1 = ['ami','tumi','bhai','bon']

list1.append('kamal')
print(list1)

# insert method

list2 = ['baba', 'ma', 'bhai', 'bon']
list2.insert(1,"mashe")
list2.insert(3,"pishe")
print(list2)


# Remove list items 

li = [52,12,48,75,25]
li.remove(12)
print(li)


# pop method removes the last item.

lis = ['112','12','1']
lis.pop(1)
print(lis)

# del method 
list3 = ['ami', 'tumu','tum']
del list3[0]
print(list3)
del list3
# print(list3)

# clear method 
li.clear()
print(li)

del li 
print(li)
