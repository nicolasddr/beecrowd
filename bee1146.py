x = int(input())

i = 1

while x != 0:
    while i <= x:
        if i < x:
            print(f'{i} ', end="")
        else:
            print(f'{i}')
        i = i + 1
    
    i = 1
    x = int(input())

    
   