import math

def TrianglePS(a):
    p = 3 * a
    s = (a ** 2) * math.sqrt(3) / 4
    return p, s
print(TrianglePS(5))
