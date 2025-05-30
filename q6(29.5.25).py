list=[1,2,3,4,5,6,7,8,9]
sqlist=[]
for i in list:
    if i%2==0:
        sqlist.append(i**2)
print(sqlist)