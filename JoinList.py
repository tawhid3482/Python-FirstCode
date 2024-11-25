list1 = ['a','b','c']
list2= [1,2,3,5]
#  + method for join list 
list3 = list1 + list2
print(list3)

# extend method for join list
list1.extend(list2)
print(list1)

# append method for join list
for i in list2:
 list1.append(i)
 print(list1)