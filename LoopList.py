# for loop

list = ['saikat','tawhidul','islam','dev','python']

for i in list:  
 print(i)

    
    # Use the range() and len() functions to create a suitable iterable. 
    
for i in range(len(list)):
    print(i) 

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes. 

x = 0
while x < len(list):
    print(list[x])
    x = x + 1

