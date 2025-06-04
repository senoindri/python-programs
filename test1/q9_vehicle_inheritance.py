#Q9. Create a class hierarchy where Vehicle is the base class, and Car and Bike inherit from it. Override a method get_type() in both. Use super() where applicable.
class Vehicle:
    def get_type(self):
        print('in vehicle')
class Car(Vehicle):
    def get_type(self):
        print('in car')
        super().get_type()
class Bike(Vehicle):
    def get_type(self):
        print('in bike')
        super().get_type()
obj=Bike()
obj.get_type()