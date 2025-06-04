#Q5. Create a generator function that yields squares of numbers from 1 to n which are divisible by 3.
def sq_div_by_3 (n):
    for i in range(n):
        if i%3==0:
            yield i
for i in sq_div_by_3(10):
    print(i)