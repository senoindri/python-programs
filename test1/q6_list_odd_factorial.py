#Q6. Use map, filter, and reduce to compute the factorial of odd numbers in a list.
l=[1,2,2,3,4,5,6,7,7,7,8,9,4,3,2,1,4,6,7,9]
l1=list(filter(lambda x:x%2!=0,l))
from functools import reduce
l2=list(map(lambda a:reduce(lambda x,y:x*y,range(1,a+1)),l1))
print(l1)
print(l2)