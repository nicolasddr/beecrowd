m, n = map(int, input().split())

maiorMN = (m + n + abs(m - n))/2
menorMN = (m + n - abs(m - n))/2

menorMN = int(menorMN)
maiorMN = int(maiorMN)

while n > 0 and m > 0:
    for i in range(menorMN, maiorMN+1):
        print(f'{i} ', end="")
        i = i + 1

    soma = sum(range(menorMN, maiorMN+1))
    print(f'Sum={soma}')

    m, n = map(int, input().split())

    maiorMN = (m + n + abs(m - n))/2
    menorMN = (m + n - abs(m - n))/2

    menorMN = int(menorMN)
    maiorMN = int(maiorMN)

    