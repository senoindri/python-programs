class bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
    def withdraw(self,wamt):
        if wamt>self.balance:
            print('amount cant be withdrawn')
        else:
            self.balance-=wamt
    def check(self):
        print('balance present: ',self.balance)

obj=bank(5000)
obj.deposit(1000)
obj.check()
obj.withdraw(6001)
obj.check()
obj.withdraw(2000)
obj.check()