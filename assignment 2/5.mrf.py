l=[1,2,3,4]

#map
def sq(x):
    return x**2
print(list(map(sq,l)))

#reduce
from functools import reduce
print(reduce(lambda x,y:x*y,l))

#filter
print(list(filter(lambda x:x%2==0,l)))