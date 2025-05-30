class c1:
    def f1():
        print('method f1 in c1')
class c2:
    def f2():
        print('methof f2 in c2')
class c3(c1,c2):
    def f3():
        print('method f3 of c3')
c3.f1()
c3.f2()
c3.f3()