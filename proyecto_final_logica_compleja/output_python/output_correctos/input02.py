def nand(x, y):
    return not (x and y)
def nor(x, y):
    return not (x or y)
def xnor(x, y):
    return x == y

a = False
b = False

def eq(x, y):
    return xnor(x, y)
def neq(x, y):
    return (x != y)
c = (nor(a, b) or nand(a, b))
t5 = neq(a, b)
t6 = eq(c, t5)
r = t6
print(r)