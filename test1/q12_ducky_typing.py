#Q12. Demonstrate polymorphism using duck typing by creating unrelated classes having the same method signature and iterating over them.
class music:
    def tune(self):
        print('melody')
class song:
    def tune(self):
        print('singing')
    def what_tune(person):
        person.tune()
m=music()
s=song()
for obj in [m,s]:
    song.what_tune(obj)