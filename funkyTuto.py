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

def addFunc(a = 1):
    """
    Adds 1 to a
    """
    b = a + 1
    return b

def mult(a,b):
    return a*b

def noWork():
    pass

def artistNames(*names):
    """
    Variatic parameter -> Any number of parameters
    """
    for name in names:
        print(name)

def globalFunc(y: int) -> int:
    global x
    x = y
    return x

global jin #marking this variable global, so that it can be manipulated inside functions as well.
jin = "Ginger bread"
def atmoFunc():
    global jin
    jin = "swamy"

def atmoAtmo():
    listOfGlobals = globals()
    listOfGlobals["jin"] = "Arraath"

print(jin)
atmoFunc()
print(jin)
atmoAtmo()
print(jin)
