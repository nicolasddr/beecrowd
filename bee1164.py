a = int(input())

for i in range(0, a ):
    n = int(input())
    soma = 0
    b = 1
    while b < n:
        if n % b == 0:
            soma = soma + b
        b = b + 1

    if soma == n:
        print(f'{n} eh perfeito')
    else:
        print(f'{n} nao eh perfeito')


    

    

