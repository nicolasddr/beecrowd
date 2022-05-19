hora_i, minuto_i, hora_f, minuto_f = map(int, input().split())

minutos_ti = minuto_i + (hora_i*60)
minutos_tf = minuto_f + (hora_f*60)

tempo_m = minutos_tf - minutos_ti

if tempo_m <= 0:
    tempo_m = tempo_m + (24*60)

horas = tempo_m // 60
minutos = tempo_m % 60


print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')