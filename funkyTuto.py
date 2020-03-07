def theFunco():
    print("list",sum([0,0,1]))
    print("tuple",sum((1,2,3)))
    print("String",sum({1,2,3}))

l = [5,9,8]
s = {5,9,8}
def sortingFunc():
    #Sorted returns sorted enumerated type
    print("Sorted",sorted([2,1,3]))
    print("Sorted",sorted(s))
    l.sort()
    #sort modifies the enumerated type
    print("Sort",l)

def addFunc(a):
    """
    Adds 1 to a
    """
    b = a + 1
    return b

def mult(a,b):
    return a*b

def noWork():
    pass

print(mult(2,2))
print(mult(2,"aaa"))
print(mult("a",3))
noWork()
sortingFunc()
