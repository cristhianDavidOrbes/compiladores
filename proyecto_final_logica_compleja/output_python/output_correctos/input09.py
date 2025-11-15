def nand(x, y):
    return not (x and y)
def nor(x, y):
    return not (x or y)
def xnor(x, y):
    return x == y

a = False
b = False

def both(x, y):
    return (x and y)
def either(x, y):
    return (x or y)
def diff(x, y):
    return (x != y)
t3 = both(a, b)
t4 = either(a, b)
t6 = diff(a, b)
r = ((t3 or t4) and (not t6))
print(r)