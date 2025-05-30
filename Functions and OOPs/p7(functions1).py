def test():
    print('first funtion')

test()
def test2():
    return 'oindri'
print(test2()+' sen')

def test3():
    return 'number1',5,4+5j,'a',[1,2,3]
print(test3()) #will return enclosde in a tuple
a,b,c,d,e=test3()
print(e)

def test4():
    a=5+6/7
    return a
print(test4())

def test5(a,b,c):
    d=a+b+c
    return d
print(test5(3,4,5))

def test6(a,b):
    return a+b
print(test6('oindri','sen')) #+ is also used to concatenate strings so it works
print(test6([1,2,3],[4,5,3]))

#make a function to extract all the integers from a list and make a list
l=[1,2,3,'cat','dog',[4,5,6]]
def intextract(l):
    """function to extract all ints in a list""" #gives a defn while hovering
    l1=[]
    for i in l:
        if type(i)==int:
            l1.append(i)
        elif type(i)==list:
            for j in i:
                if type(j)==int:
                    l1.append(j)
    return l1
print(intextract(l))

def sumofargs(*args): #type of this function is a tuple
    return args
print(sumofargs(1,2,3,'a',9+5j))

def args1(*args,a):
    return args,a
print(args1(1,2,3,a=4)) #a's value has to be explicitly specifies, so that its not included in *args

def test7(c,d,a=5,b=6): #wont work if c and d are later
    return a,b,c,d
print(test7(7,8))
print(test7(7,8,a=0)) #overrides a

#to pass dict value
def test8(**kwargs):
    return kwargs
print(test8(a='goat',b=23,c=0.6))