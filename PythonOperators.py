# Python Operators
''' 
 Arithmetic Operator
 Assignment 
 Comparison
 Logical
 Identify
 Membership
 Bitwise

'''

# Arithmetic Operators
x = [25,45,85,14,25,425] 

print(x[0]+ x[5])  #Addition
print(x[2]- x[3])  #Subtraction
print(x[2]* x[3])  #Multiplication
print(x[2] / x[3])  #Division
print(x[1] % x[3])  #Division
print(x[1] ** x[3])  #Exponentiation
print(x[1] // x[3])  #Floor division


# assignment operator

y = 10
y += 5
y-=5
y*=2
y/=2
y%=3

y//=3

y **= 25
y&=10
y|=5
y^=5
y >>= 3
y <<= 3

print(y:= 3)

# Comparison Operators 

a = 10
b = 5
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)


# Swapping 

c = 5 
d = 3
c,d = d,c
print(c,d)