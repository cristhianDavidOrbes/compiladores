def nand(x, y):
    return not (x and y)
def nor(x, y):
    return not (x or y)
def xnor(x, y):
    return x == y

a = False
b = False

def flipIf(cond):
    a = False
    b = False
    if cond:
        a = (not a)
    else:
        b = (not b)
a = True
b = False
c = (a != b)
flipIf(c)
ok = (a or b)
print(ok)