
i = 0

while True:
    
    jogadas = int(input())

    if jogadas == 0:
        break

    jogador_1 = input()
    jogador_2 = input()
    
    vencedor = []
    
    for h in range(jogadas):
        a, b = map(int, input().split())

        if (a + b) % 2 == 0:
            vencedor.append(jogador_1)
        else:
            vencedor.append(jogador_2)
    
    print('Teste {}' .format(i+1))
    for v in range(jogadas):
        print(vencedor[v])
    print("")

    i = i + 1



