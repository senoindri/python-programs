#Q2. Check if a given integer is a palindrome without converting it to a string.
n=int(input('enter number'))
copy,palin=n,0
while copy>0:
    r=copy%10
    palin=palin*10+r
    copy=int(copy/10)
if palin==n:
    print('it is a palindrome')
else:
    print('it is not a plaindrome')