def sumofargs(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sumofargs(5,8,9,0.5,6))