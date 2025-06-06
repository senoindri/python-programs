#Q5. What are Custom Exceptions in python? Why do we need Custom Exceptions? Explain with an example.
#A. Custom exceptions are exceptions created by the user, due to cases that are syntactically correct but logically incorrecct and cannot be detected by the compilor
class agevalid(Exception):
    def __init__(self, msg):
        self.msg=msg
def isagevalid(n):
    if n<0:
        raise agevalid("bro doesn't even exist")
    elif n>200:
        raise agevalid('dont lie')
    else:
        print('ok')
try:
    age=int(input('how old r u '))
    isagevalid(age)
except agevalid as e:
    print (e)