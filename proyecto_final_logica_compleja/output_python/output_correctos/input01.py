def nand(x, y):
    return not (x and y)
def nor(x, y):
    return not (x or y)
def xnor(x, y):
    return x == y

def id(x):
    return x
a = True
b = False
t4 = id(((a and (not b)) or (a != b)))
r = t4
print(r)