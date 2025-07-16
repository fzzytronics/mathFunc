from math import *

print("Choose a shape to calculate area, volume of the shape revolved around the y-axis, and surface area of that 3D shape:")
print("1. Circle")
print("2. Rhombus Prism")
print("3. Triangle Cone")
print("4. Rectangle Cylinder")

choice = input("Enter the number of your choice: ")

if choice == "1":
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

elif choice == "2":
    def rhombus_area(p, q):
        area = (p * q)
        return area

    def rhombus_volume(p, q, h):
        volume = rhombus_area(p, q) * h
        return volume

    def rhombus_surfaceArea(p, q, h):
        surf = (2*(rhombus_area(p,q)))+((2*p)+(2*q))*h
        return surf

    p = float(input(f'Side 1 of rhombus: '))
    q = float(input(f'Side 2 of rhombus: '))
    h = float(input(f'Height of prism: '))

    print(f'The area of the rhombus is =', rhombus_area(p,q))
    print(f'The volume of the rhombus prism is =', rhombus_volume(p,q,h))
    print(f'The volume Surface Area =', rhombus_surfaceArea(p,q,h))

elif choice == "3":
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

elif choice == "4":
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

else:
    print("Invalid choice\n")