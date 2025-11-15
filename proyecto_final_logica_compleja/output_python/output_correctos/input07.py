def nand(x, y):
    return not (x and y)
def nor(x, y):
    return not (x or y)
def xnor(x, y):
    return x == y

def passIf(cond, x):
    if cond:
        return x
    else:
        return (not x)
g = True
h = False
t3 = passIf(nor(g, h), (g != h))
k = t3
print(k)