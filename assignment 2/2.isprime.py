def isprime(n):
    i=2
    count=0
    while i<n:
        if n%i==0:
            count+=1
            i+=1
        else:
            i+=1
    if count>0:
        print(n,' is a composite number')
    else:
        print(n,' is a prime number')
isprime(121)