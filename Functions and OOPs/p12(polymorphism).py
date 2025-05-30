class data_science:
    def syllabus(self):
        print('data science syllabus')
class web_dev:
    def syllabus(self):
        print('web dev syllabus')
def class_parcer(class_obj):
    for i in class_obj:
        i.syllabus()
data_science=data_science()
web_dev=web_dev()
class_obj =[data_science,web_dev]
class_parcer(class_obj)