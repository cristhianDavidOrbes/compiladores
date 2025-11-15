def nand(x, y):
    return not (x and y)
def nor(x, y):
    return not (x or y)
def xnor(x, y):
    return x == y

a = False
b = False

def mix(x, y):
    t = nand(x, y)
    if t:
        t = nor(x, y)
    else:
        t = xnor(x, y)
    return t
t3 = mix(a, b)
z = t3
print(z)