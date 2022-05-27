
while True:
    
    n = int(input())

    if n == 0:
        break

    comando = input().split()

    direcao = 'N'

    i = 0
    while i < n:
        if comando[i] == 'D' and direcao == 'N':
            direcao = 'L'
        elif comando[i] == 'D' and direcao == 'S':
            direcao = 'O'
        elif comando[i] == 'D' and direcao == 'L':
            direcao = 'S'
        elif comando[i] == 'D' and direcao == 'O':
            direcao = 'N'
        elif comando[i] == 'E' and direcao == 'N':
            direcao = 'O'
        elif comando[i] == 'E' and direcao == 'S':
            direcao = 'L'
        elif comando[i] == 'E' and direcao == 'L':
            direcao = 'N'
        elif comando[i] == 'E' and direcao == 'O':
            direcao = 'S'
        else:
            print('TA ERRADO BURRO')

        i = i + 1

    print(direcao)
    

    

