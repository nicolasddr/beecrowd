
t = 0

while True:

    x1, y1, x2, y2 = map(int, input().split())

    if x1 == y1 == x2 == y2 == 0:
        break

    n = int(input()) 
    qtd = 0
    
    for i in range(n):
        x, y = map(int, input().split())

        if x1 <= x and x2 >= x and y1 >= y and y2 <= y:
            qtd = qtd + 1
        else:
            qtd = qtd
    
    
    print('Teste {}' .format(t+1))
    print(qtd)

    t = t + 1
