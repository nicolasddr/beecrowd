numero_de_casos = int(input())

for i in range(0, numero_de_casos):
    pa, pb, g1, g2 = input().split()

    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)/100
    g2 = float(g2)/100

    anos = 0

    while pa <= pb and anos <= 100:
        
        pa = pa + int((pa * g1))
        pb = pb + int((pb * g2))

        anos = anos + 1

    if anos <= 100:
        print(f'{anos} anos.')
    else:
        print('Mais de 1 seculo.')





