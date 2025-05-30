def fac_rec(n):
    if n>0:
        return n*fac_rec(n-1)
    else:
        return 1
print(fac_rec(4))