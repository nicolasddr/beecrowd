c1 = input()
c2 = input()
c3 = input()

if c1 == "vertebrado":
    if c2 == "ave":
        if c3 == "carnivoro":
            print('aguia')
        else:
            print('pomba')
    else:
        if c3 == "onivoro":
            print('homem')
        else:
            print('vaca')
else:
    if c2 == "inseto":
        if c3 == "hematofago":
            print('pulga')
        else:
            print('lagarta')
    else:
        if c3 == "hematofago":
            print('sanguessuga')
        else:
            print('minhoca')
