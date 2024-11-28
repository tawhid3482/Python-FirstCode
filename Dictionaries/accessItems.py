dictionary ={ "name":"saikat","age":"25","isMaried":"false"}

x = dictionary['name']
y = dictionary['age']
print(x,y)


# get method  There is also a method called get() that will give you the same result:

z = dictionary.get('age')
print(z)

# keys method sokol keys nam dibe
a = dictionary.keys()
print(a)

#  new keys vule add korar jnno
dictionary["education"]="diploma"
print(dictionary)

# values method sokol values nam dibe
a = dictionary.values()
print(a)

# sob items gula juray juray dakhabe
b = dictionary.items()
print(b)


info = {
   "student1" :{
       "name":"saikat",
       "age":"25",
       "isMaried":"false"
       },
   "student2" :{
       "name":"tomal",
       "age":"22",
       "isMaried":"true"
       },
   "student3" :{
       "name":"tumu",
       "age":"21",
       "isMaried":"false"
       }
}

print(info["student2"])
print(info["student2"]["name"])