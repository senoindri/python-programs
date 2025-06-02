#1
class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

#2
class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity} passengers."
my_car = Car("Honda City", 180, 15)
print(my_car.seating_capacity(5))

#3
class Father:
    def skills(self):
        print("Father: Gardening, Teaching")

class Mother:
    def skills(self):
        print("Mother: Cooking, Art")

class Child(Father, Mother):
    def skills(self):
        print("Child: ", end="")
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.skills()

#4
class Student:
    def __init__(self):
        self.__name = ""

    def get_name(self):  # Getter
        return self.__name

    def set_name(self, name):  # Setter
        self.__name = name

s = Student()
s.set_name("Alice")
print("Student Name:", s.get_name())

#5
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Overriding
        print("Dog barks")

a = Animal()
a.speak()

d = Dog()
d.speak()