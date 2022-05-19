a, dia_i = input().split()
hora_i, minuto_i, segundo_i = map(int, input().split(" : "))
b, dia_f = input().split()
hora_f, minuto_f, segundo_f = map(int, input().split(" : "))

dia_i = int(dia_i)
dia_f = int(dia_f)

segundos_ti = (dia_i*24*60*60) + (hora_i*60*60) + (minuto_i*60) + segundo_i
segundos_tf = (dia_f*24*60*60) + (hora_f*60*60) + (minuto_f*60) + segundo_f

segundos = segundos_tf - segundos_ti

minutos = segundos // 60
segundos = segundos % 60

horas = minutos // 60
minutos = minutos % 60

dias = horas // 24
horas = horas % 24

print(f"""{dias} dia(s)
{horas} hora(s)
{minutos} minuto(s)
{segundos} segundo(s)""")
