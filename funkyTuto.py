def theFunco():
    print("list",sum([0,0,1]))
    print("tuple",sum((1,2,3)))
    print("String",sum({1,2,3}))

l = [5,9,8]
s = {5,9,8}
def sortingFunc():
    print("Sorted",sorted([2,1,3]))
    print("Sorted",sorted(s))
    l.sort()
    print("Sort",l)

sortingFunc()
