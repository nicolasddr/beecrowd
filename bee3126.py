c = int(input())
lista = input().split()

quantidade = 0

for i in range(c):
    if lista[i] == "1":
        quantidade = quantidade + 1
    else:
        quantidade = quantidade

print(quantidade)