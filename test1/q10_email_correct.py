#Q10. Implement a class using property decorators to validate that an email is set in the right format.
class test:
    def __init__(self,email):
        self.__email=email
    @property
    def email_access(self):
        return self.__email
    @email_access.getter
    def email_getter(self):
        if self.__email[-9::1]=='gmail.com':
            return True
        else:
            return False
t=test(input('input email id '))
print(t.email_access)
print(t.email_getter)