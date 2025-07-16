from math import *

r = float(input(f'radius of circle: '))

def area():
    area = pi * r**2
    print(area)

area()

def volume():
    volume = (4/3) * pi * r**3
    print(volume)

volume()

def surfaceArea():
    surfaceArea = 4 * pi * r**2
    print(surfaceArea)

surfaceArea()
