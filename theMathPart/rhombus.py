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