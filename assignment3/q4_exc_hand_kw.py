#Q4. Explain with an example:
#try and else#
#finally
#raise

try:
    print(10/1)
except ZeroDivisionError as e:
    print('cant ',e)
else:
    print('this is printed if try block generates no error')
finally:
    print('this will execute itself in every situation, regarless of exception generation')

#in case of custom erors, the raise keyword is used to intentionally generate exceptions. in case of logical errors that might generate an exception, user-defined custom errors are required, and raise is used to generate errors in those situations. 
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
    isagevalid(-1)
except agevalid as e:
    print (e)