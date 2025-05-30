def test():
    print('start func')
    print('functo test')
    print(4*5)
    print('end func')
test()

def deco(test):
    def inner_deco():
        print('start func')
        test()
        print('end func')
    return inner_deco

@deco
def test1():
    print(6+7)
test1()

import time
def timer_test(func):
    def inner_timer_test():
        start=time.time()
        func()
        end=time.time()
        print(end-start)
    return inner_timer_test

@timer_test
def test2():
    print(45+78)  
test2()

@timer_test
def test3():
    for i in range(10000000000):
        pass