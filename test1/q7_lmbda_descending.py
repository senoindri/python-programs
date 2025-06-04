#Q7. Write a higher-order function that accepts a list and a lambda, applies the lambda, and returns a list of unique results sorted in descending order.
def unique_descending(l,a):
    result=list(map(a,l))
    result=list(set(result))
    result.sort(reverse=True)
    return result
l=[1,1,2,2,2,3,4,5,5,4,5,6]
a=lambda x:x**2
print(unique_descending(l,a))