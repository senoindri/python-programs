class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
t=test(23,34)
t.a=90 #not private
print(t.a)

class car:
    def __init__(self,year,model,speed):
        self.__year=year #now private
        self.__model=model
        self.__speed=speed
    def set_speed(self,speed): #no pvt, invoked first
        self.__speed=0 if speed<0 else speed 
    def get_speed(self):
        return self.__speed
c=car(2021,'audi','24sl')
print(c._car__year) #can only access like this
c.set_speed(-90)
print(c.get_speed()) #wont since -ve
c.set_speed(50)
print(c.get_speed()) #works

class bank_account:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
            return True
        else:
            return False
    def get_balance(self):
        return self.__balance
    
oindri=bank_account(1000)
print(oindri.get_balance())
oindri.deposit(5000)
print(oindri.get_balance())
print(oindri.withdraw(200))
print(oindri.get_balance())