import abc
class test:

    @abc.abstractmethod
    def student_details(self):
        pass

    @abc.abstractmethod
    def student_assignment(self):
        pass
        
    @abc.abstractmethod
    def student_marks(self):
        pass

class stu_det(test):
    def student_details(self):
        print('method to take student details')
    def student_assignment(self):
        print('method to take student assignments')

class masters(test):
    def student_details(self):
        print('master-student details')
    def student_marks(self):
        print('master-student marks')

obj2=masters()
obj2.student_marks()