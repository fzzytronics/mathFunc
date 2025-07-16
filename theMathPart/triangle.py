from math import *

b = float(input(f'base of triangle: '))
h = float(input(f'height of triangle: '))
r = b


j = float(r**2)
k = float(h**2)

def triArea():
    triArea = (1/2) * b * h
    print(triArea)
triArea()

def triVol():
    triVol = (1/3) * pi * r**2 * h
    print(triVol)
triVol()

def triSurfaceArea():
    triSArea = pi * r * (r + (sqrt(j*k)))
    print(triSArea)
triSurfaceArea()
