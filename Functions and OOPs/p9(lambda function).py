#normal function to number raised to power
def pow1(n,p):
    return n**p
print(pow1(2,3))

#lambda functinot to do the same
a= lambda n,p: n**p 
print(a(2,3))

add= lambda x,y: x+y
print(add(4,5))

#celcius to fahrenheit
f=lambda c:c*9/5+32
print(f(45))

#max of 2 nos
max=lambda x,y: x if x>y else y
print(max(9,8))

#length of string
length=lambda s:len(s)
print(length('oindri'))