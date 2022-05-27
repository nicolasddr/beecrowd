
while True:
    try:
        n = int(input())

        epr = 0
        ehd = 0
        intrusos = 0

        for i in range(n):
            matricula, sigla = input().split()
            
            if sigla == 'EPR':
                epr = epr + 1
            elif sigla == 'EHD':
                ehd = ehd + 1
            else:
                intrusos = intrusos + 1

        print('EPR: {}' .format(epr))
        print('EHD: {}' .format(ehd))
        print('INSTRUSOS: {}' .format(intrusos))

    except EOFError:
        break
