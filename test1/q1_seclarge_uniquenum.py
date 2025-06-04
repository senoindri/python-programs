#Q1. Find the second largest unique number in a list without using set.
l=[1,2,2,3,4,3,5,6,7,7,8,1] #->should give 6
l2=[] #to hold the unique numbers 
for i in l:
    c=l.count(i)
    if c==1:
        l2.append(i)
print(l2[-2])