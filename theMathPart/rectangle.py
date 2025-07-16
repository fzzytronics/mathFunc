from math import *

x = float(input(f'Side 1 of rectangle: '))
y = float(input(f'Side 2 of rectangle: '))
r = x


def sqrArea():
    sqrArea = x * y
    print(sqrArea)
sqrArea()

def sqrVol():
    sqrVol = pi * r**2 * y
    print(sqrVol)
sqrVol()

def sqrSArea():
    sqrSArea = (2 * pi * r**2) + (2 * pi * r * y)
    print(sqrSArea)
sqrSArea()