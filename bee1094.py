n = int(input())

coelhos = 0
ratos = 0
sapos = 0
total = 0

for i in range(0, n):
    qtd, tipo = input().split()
    qtd = int(qtd)

    if tipo == "C":
        coelhos = coelhos + qtd
    if tipo == "R":
        ratos = ratos + qtd
    if tipo == "S":
        sapos = sapos + qtd
    
    total = total + qtd

percentual_coelhos = (coelhos/total)*100
percentual_ratos = (ratos/total)*100
percentual_sapos = (sapos/total)*100

print(f"""Total: {total} cobaias
Total de coelhos: {coelhos}
Total de ratos: {ratos}
Total de sapos: {sapos}
Percentual de coelhos: {percentual_coelhos:.2f} %
Percentual de ratos: {percentual_ratos:.2f} %
Percentual de sapos: {percentual_sapos:.2f} %""")