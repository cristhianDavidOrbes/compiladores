def nand(x, y):
    return not (x and y)
def nor(x, y):
    return not (x or y)
def xnor(x, y):
    return x == y

a = False
b = False

def spinUntilEqual(x, y):
    while ((x or y) and (not xnor(x, y))):
        y = (not y)
        if xnor(x, y):
            break
        else:
            continue
spinUntilEqual(a, b)
c = xnor(a, b)
d = ((a or b) and (not (a != b)))
print(c)
print(d)