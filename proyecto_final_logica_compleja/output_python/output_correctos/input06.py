def nand(x, y):
    return not (x and y)
def nor(x, y):
    return not (x or y)
def xnor(x, y):
    return x == y

def reduce3(x, y, z):
    return (((x and (not y)) or (z and (x != y))) and xnor(x, z))
a = True
b = True
c = False
t7 = reduce3(a, b, c)
out = t7
print(out)