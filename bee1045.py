
x, y, z = map(float, input().split())

if x >= y and x >= z:
    a = x
    b = y
    c = z

if y >= x and y >= z:
    a = y
    b = x
    c = z

if z >= x and z >= y:
    a = z
    b = x
    c = y   

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    
    if (a**2) > (b**2) + (c**2):
        print("TRIANGULO OBTUSANGULO")
    elif (a**2) < (b**2) + (c**2):
        print("TRIANGULO ACUTANGULO")
    else:
        print("TRIANGULO RETANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")
