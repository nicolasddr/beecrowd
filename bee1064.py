v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())

NumerosPositivos = []
qtdPositivos = 0 
qtdNegativos = 0


# Verifica se os numeros são positivos ou não
if v1 > 0:
    qtdPositivos = qtdPositivos + 1
    NumerosPositivos.append(v1)
else:
    qtdNegativos = qtdNegativos + 1

if v2 > 0:
    qtdPositivos = qtdPositivos + 1
    NumerosPositivos.append(v2)
else:
    qtdNegativos = qtdNegativos + 1

if v3 > 0:
    qtdPositivos = qtdPositivos + 1
    NumerosPositivos.append(v3)
else:
    qtdNegativos = qtdNegativos + 1

if v4 > 0:
    qtdPositivos = qtdPositivos + 1
    NumerosPositivos.append(v4)
else:
    qtdNegativos = qtdNegativos + 1

if v5 > 0:
    qtdPositivos = qtdPositivos + 1
    NumerosPositivos.append(v5)
else:
    qtdNegativos = qtdNegativos + 1

if v6 > 0:
    qtdPositivos = qtdPositivos + 1
    NumerosPositivos.append(v6)
else:
    qtdNegativos = qtdNegativos + 1

# Soma os números positivos e cálcula a média
SomaPositivos = sum(NumerosPositivos)
MediaPositivos = SomaPositivos/qtdPositivos


print(f'{qtdPositivos} valores positivos')
print(f'{MediaPositivos:.1f}')