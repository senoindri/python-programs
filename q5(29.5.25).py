list=[1,2,2,2,1,1,3,3,3,4,4,3,5,3,5,5,6,3,3,6,6,1]
newlist=[]
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)