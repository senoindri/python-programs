#1
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# Creating an object
my_dog = Dog("Tommy", "Labrador")
my_dog.bark()  # Output: Tommy is barking!

#2
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

s = Student("John", 101)
s.show()  # Output: Name: John, Roll: 101

#3
class Circle:
    def __init__(self, radius):
        self.radius = radius  # self.radius refers to the instance variable

    def area(self):
        return 3.14 * self.radius ** 2

#4
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

d = Dog()
d.sound()
d.bark()

#multiple
class Father:
    def skill(self):
        print("Gardening")

class Mother:
    def skill(self):
        print("Cooking")

class Child(Father, Mother):
    def play(self):
        print("Playing Football")

c = Child()
c.skill()  # Executes Father's skill (due to MRO)

#multilevel
class Grandparent:
    def family_name(self):
        print("Smith")

class Parent(Grandparent):
    def home(self):
        print("Big House")

class Child(Parent):
    def school(self):
        print("International School")

c = Child()
c.family_name()
c.home()
c.school()

#heirarchical
class Vehicle:
    def start(self):
        print("Engine Started")

class Car(Vehicle):
    def wheels(self):
        print("4 Wheels")

class Bike(Vehicle):
    def wheels(self):
        print("2 Wheels")

c = Car()
b = Bike()
c.start()
c.wheels()
b.start()
b.wheels()

#hybrid inheritance
class A:
    def method_A(self):
        print("Class A")

class B(A):
    def method_B(self):
        print("Class B")

class C:
    def method_C(self):
        print("Class C")

class D(B, C):
    def method_D(self):
        print("Class D")

d = D()
d.method_A()
d.method_C()
d.method_D()
