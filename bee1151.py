
n = int(input())

n1 = 0
n2 = 1
i = 3

print('0 1 ', end="")

while i <= n:
    n3 = n1 + n2
    if i < n:
        print(f'{n3} ', end="")
    else:
        print(f'{n3}')
    n1 = n2
    n2 = n3
    i = i + 1