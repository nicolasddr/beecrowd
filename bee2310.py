
n = int(input())

saque_total = 0
pontos_saque = 0

bloqueio_total = 0
pontos_bloqueio = 0

ataque_total = 0
pontos_ataque = 0

i = 0
while i < n:
    nome = input()
    s, b, a = map(int, input().split())
    s1, b1, a1 = map(int, input().split())

    saque_total = saque_total + s
    pontos_saque = pontos_saque + s1

    bloqueio_total = bloqueio_total + b
    pontos_bloqueio = pontos_bloqueio + b1

    ataque_total = ataque_total + a
    pontos_ataque = pontos_ataque + a1

    i = i + 1


percentual_saque = (pontos_saque/saque_total)*100
percentual_bloqueio = (pontos_bloqueio/bloqueio_total)*100
percentual_ataque = (pontos_ataque/ataque_total)*100

print('Pontos de Saque: {:.2f} %.' .format(percentual_saque))
print('Pontos de Bloqueio: {:.2f} %.' .format(percentual_bloqueio))
print('Pontos de Ataque: {:.2f} %.' .format(percentual_ataque))