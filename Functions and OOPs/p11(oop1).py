class test:
    pass
a=test()
print(type(a))

class cat:
    def what(self):
        print('feline')
billy=cat()
print(type(billy))
billy.what()
garfield=cat()
garfield.what()

class test:
    def __init__(self,phone_no,email_id):
        self.phone_no1=phone_no
        self.email_id1=email_id
    def return_student_details(self):
        return self.phone_no1,self.email_id1 

nikasha=test(9098,'niki@gmail.com')
print(nikasha.return_student_details()) #prints nikashas details
print(nikasha.phone_no1)
print(nikasha.email_id1)