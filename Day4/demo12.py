def printMax(a,b):
        if a > b:
                print a, 'is maximum'
        else:
                print b, 'is maximum'

def getMax(a,b):
        if a > b:
                return a
        return b

# printMax(3,4)
# printMax(5,7)
# printMax(10,12)

mymax = getMax(10, 12)
print mymax
