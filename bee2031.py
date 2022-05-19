casos = int(input())

for i in range(casos):
    J1 = input()
    J2 = input()
    
    if J1 == "ataque" and J2 == "pedra":
        print('Jogador 1 venceu')
    elif J1 == "pedra" and J2 == "papel":
        print('Jogador 1 venceu')
    elif J1 == "papel" and J2 == "ataque":
        print('Jogador 2 venceu')
    elif J1 == "pedra" and J2 == "ataque":
        print('Jogador 2 venceu')
    elif J1 == "papel" and J2 == "pedra":
        print('Jogador 2 venceu')
    elif J1 == "ataque" and J2 == "papel":
        print('Jogador 1 venceu')
    elif J1 == "papel" and J2 == "papel":
        print('Ambos venceram')
    elif J1 == "ataque" and J2 == "ataque":
        print('Aniquilacao mutua')    
    else:
        print('Sem ganhador')

