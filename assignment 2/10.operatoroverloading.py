class point:
    def __init__(self,p):
        self.p=p
    def __add__(self,point):
        return self.p+point.p
obj=point(9.8)
obj1=point(0.2)
print(obj+obj1)