#1
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print("Area of circle:", c.area())

#2 
#encapsulation
class Person:
    def __init__(self):
        self.__age = 0  # private variable

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

p = Person()
p.set_age(25)
print(p.get_age())

#3
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

#4
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def mileage(self):
        pass

class Bike(Vehicle):
    def mileage(self):
        print("Mileage is 60 kmpl")

b = Bike()
b.mileage()