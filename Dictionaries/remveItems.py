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


info.pop("student3")
print(info)

# remove last items
info.popitem()
print(info)

del info['student1']
print(info)

del info 
print(info)

info.clear()
print(info)
