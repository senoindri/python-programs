#square a list
l=[1,2,3,4]
def test(l):
    l1=[]
    for i in l:
        l1.append(i**2)
    print(l1)
test(l)

#MAP - alternative of for i in l
def sq(x):
    return x**2
print(list(map(sq,l))) #map(func,interable), maps the function over the interable entity

print(list(map(lambda x:x**2,l))) #works for external func, also lambda func

#add each indexes
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
print(list(map(lambda x,y: x+y, l1,l2))) #1 func, 2 iterables, takes x from l1, y from l2 then adds

#incase u want to use external functions
def add(x,y):
    return x+y
print(list(map(add,l1,l2)))

string='cat' #to convert to upper using mapped function
print(list(map(lambda x:x.upper(), string)))

#REDUCE - not implicitly present, have to import
from functools import reduce
l=[1,2,3,4]
print(reduce(lambda x,y:x+y,l))

print(reduce(lambda x,y:x+y, [1])) #can work with only 1 element also, but cant take >2 parameters 

print(reduce(lambda x,y:x*y,l))
print(reduce(lambda x,y:x*y,[2,3]))

#find max in list using reduce
print(reduce(lambda x,y: x if x>y else y, l))

#FILTER - 
print(list(filter(lambda x: x%2==0,l))) #prints even no.s
print(list(filter(lambda x:x%2!=0,l))) #prints odd no.s

l1=[-1,-5,6,7,-8,-9,0] #print negatives
print(list(filter(lambda x:x<0,l1)))

l3=['oindri','anindya','amrita','nabarun']
print(list(filter(lambda x:len(x)<=6,l3)))