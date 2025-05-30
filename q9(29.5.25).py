mark=int(input("enter mark of student: "))
if mark>=70:
    print('A grade')
elif mark<70 and mark>=40:
    print('B grade')
elif mark<40 and mark>=10:
    print('C grade')
else:
    print('fail')