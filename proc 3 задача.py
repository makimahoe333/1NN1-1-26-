import math
def mean(X,Y,Amean,Gmean):
    AMean = (X + Y) / 2
    GMean = math.sqrt(X * Y)
    return AMean, GMean
print(mean(4,9,0,0))
