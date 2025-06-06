#Q4. Why LookupError class is used? Explain with an example KeyError and IndexError.
#A. LookupError is the base class for look up errors. when a key/index used on a mapping/sequence is invalid, it generates a lookuperror, i.e. it is a bseclass for failed lookups.

try:
    d={1:"a",2:"b",3:"c"}
    print(d[4])
except KeyError as e:
    print('so',e)

try:
    a=[1,2,3,4,5]
    print(a[5])
except IndexError as e:
    print('and',e)