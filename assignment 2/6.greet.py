class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print('hello ',self.name,' you are ',self.age,'years old')
p=Person('oindri',18)
p.greet()