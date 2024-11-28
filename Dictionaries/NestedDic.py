Product = {
  "pro1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "pro2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "pro3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


product1 = {
"name":"apple",
"color":"red",
"price":10,
"expired":"2 days"
}
product2 = {
"name":"grapes",
"color":"red",
"price":12,
"expired":"3 days"
}
product3 = {
"name":"mango",
"color":"yellow",
"price":8,
"expired":"7 days"
}

myProducts= {
    "pro1":product1,
    "pro2":product2 ,
    "pro3":product3 ,
}
# print(myProducts)

# print(myProducts["pro3"]["name"])

for i, obj in myProducts.items():
    print(i)
    
for x in obj:
    print(x + ":", obj[x])
