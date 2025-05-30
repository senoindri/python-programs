#to create a generator funcitno use yield 

range(0,10)
for i in range(10):
    print(i)

#print n fibonacci numbers
def fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
print(fib(10)) #wont give output like this as it only creates an object
for i in fib(10):
    print(i)

#same use for loop
def fib1():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
testfib=fib1()
for i in range(10):
    print(next(testfib))

def count_test(n):
    count=1
    while count<n:
        yield count
        count+=1
c=count_test(5)
# print(c) wont work as it will just create object, so it has to be printed inside loop
for i in c:
    print(i)