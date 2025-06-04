#Q3. Given a list of integers, return the frequency count in a dictionary, sorted by frequency in descending order.
d={}
l=[1,1,2,2,2,2,3,4,4,4,5,6,7,7,7,8,1,8]
for i in l:
    d[i]=d.get(i,0)+1
sort=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
print(sort)