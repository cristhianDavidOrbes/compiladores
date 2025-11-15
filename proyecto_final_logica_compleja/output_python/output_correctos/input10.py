def nand(x, y):
    return not (x and y)
def nor(x, y):
    return not (x or y)
def xnor(x, y):
    return x == y

def inner(x):
    w = (not x)
    return w
def outer(p, q):
    t1 = inner(q)
    if ((p and (not q)) or (((p and t1) and ((not q) or p)) and (p != q))):
        return nor(p, q)
    else:
        return xnor(p, q)
a = True
b = False
c = (a != b)
t14 = outer(a, c)
ans = t14
print(ans)