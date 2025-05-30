class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print('hello ',self.name,' you are ',self.age,'years old')
class Student(Person):
    def bye(self):
        print('bye ',self.name)
s=Student('mia',26)
s.greet()
s.bye()