# String type data 

StringType = 'Hi My name is Tawhidul Islam'

print(StringType)


# int type data 

IntType = 25

print(IntType)
print(type(IntType))

# floating type 
FloatType = 20.9
print(type(FloatType))

# complex type 

ComplexType = 15565j
print(type(ComplexType))


# str data type 

myName ='Tawhidul Islam'
print("My name is"+ ' '+ myName)

# boolean type  

booleanType = True
print(booleanType) 
print(type(booleanType)) 

x =8 
y= 8
print(x >= y)
print(x == y)

# string formatting 

num1 = 25 
num2 = 14
print(f"add the number  {num1 + num2}")
print(f"add the number  {num1 - num2}")
print(f"add the number  {50 * 15}")
print(f"my name is  {myName}")

# Binary types 
# bytes type immutable
listOfNumber = [1,12,51,25,2,45,45,255]
b = bytes(listOfNumber)
print(type(b))


# bytearray mutable
listOfNumber = [1,12,51,25,2,45,45,]
b1 = bytearray(listOfNumber)
b1[0]=10
print(b1[0])
print(type(b1))


# none type data 
x = None
print(x)
print(type(x))
