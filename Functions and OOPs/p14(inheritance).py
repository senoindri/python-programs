class test:
    def test_method(self):
        print('first method')
class child_test(test):
    pass
obj=child_test()
obj.test_method()

class class1:
    def test_class1(self):
        return "method from class1"
class class2(class1):
    def test_class2(self):
        return "method from class2"
class class3(class2):
    pass
obj1=class3()
print(obj1.test_class1())
print(obj1.test_class2())

#multiple inheritance
class classa:
    def classa_method(self):
        print('class a')
class classb:
    def classb_method(self):
        print('class b')
class classc(classa,classb):
    pass
obj2=classc()
obj2.classa_method()
obj2.classb_method()