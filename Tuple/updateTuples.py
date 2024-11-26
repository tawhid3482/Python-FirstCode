tup = ('mai','i','am','saikat')

# tuple k list a convert kore list ar sob kora jay 1
x = list(tup)
x.append('developer')
y = tuple(x)
print(y)
# del tup     tuple delete kora jay 2

# remove  3
x = list(tup)
x.remove('mai')
z = tuple(x)
print(z)

# remove 4
x = list(tup)
x.pop(1)
y = tuple(x)
print(y)


thisTup = (1,5,1,4,2,36,7)
z = ("orange",'kamal')
thisTup += z
print(thisTup)