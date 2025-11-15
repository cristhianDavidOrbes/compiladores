def nand(x, y):
    return not (x and y)
def nor(x, y):
    return not (x or y)
def xnor(x, y):
    return x == y

def gate(x, y, z):
    m = (x and (not y))
    while ((m or z) and (not (x != z))):
        z = (not z)
        m = (m != z)
    return (m or z)
t = True
u = False
t10 = gate(t, u, (t != u))
res = t10
print(res)