from re import X


a = 10
print(id(a))
def something():
    a = 9 
    X = globals()['a']
    print(id(X))
    print("in fun" ,a)

something()

print("outside", a) 