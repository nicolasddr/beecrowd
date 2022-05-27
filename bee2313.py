a, b, c = map(int, input().split())

if a > b and a > c:
    hipotenusa = a
    cateto_1 = b
    cateto_2 = c
elif b > a and b > c:
    hipotenusa = b
    cateto_1 = a
    cateto_2 = c
elif c > a and c > b:
    hipotenusa = c
    cateto_1 = a
    cateto_2 = b
else:
    hipotenusa = a
    cateto_1 = b
    cateto_2 = c

if (hipotenusa**2) == (cateto_1**2) + (cateto_2**2):
    retangulo = 'Retangulo: S'
else:
    retangulo = 'Retangulo: N'


if (cateto_1 + cateto_2) > hipotenusa :
    
    if cateto_1 == cateto_2 == hipotenusa:
        print('Valido-Equilatero')
        print(retangulo)
    elif cateto_1 != cateto_2 != hipotenusa:
        print('Valido-Escaleno')
        print(retangulo)
    else:
        print('Valido-Isoceles')
        print(retangulo)
else:
    print('Invalido')

