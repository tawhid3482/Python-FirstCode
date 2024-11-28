thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for i in thisdict:
    print(i) # sudu key gula loop kore dibe
    print(thisdict[i]) # sudu value gula loop kore dibe
    
    
    # sudu value gula lagle values() use kora jabe
    
for x in thisdict.values():
    print(x)
    
    # sudu keys gula lagle keys() use kora jabe
    
for x in thisdict.keys():
    print(x)
    
        # sudu items gula lagle items() use kora jabe
        
for a in thisdict.items():
 print(a)