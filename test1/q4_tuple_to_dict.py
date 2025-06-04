#Implement a function that takes a list of tuples and groups the elements by the first element of each tuple into a dictionary of sets.
l=[('a', 1), ('b', 2), ('a', 3), ('b', 2), ('a', 1), ('c', 4)]
def listtaker(l):
    d={}
    for i in l:
        d[i[0]]=d.get(i[0],0)+1
    return d
print(listtaker(l))