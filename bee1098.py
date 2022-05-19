
j = 1
i = 0

a = 0.2
n = 0

while i <= 2:
    for k in range (1, 4):
        if i >= 2.2:
            print(f'I={j:.0f} J={j:0.f}')
        if i == 1.0 or i > 1.8 or i == 0.0:
            print(f'I={i:.0f} J={j:.0f}')
        elif i < 2:
            print(f'I={i:.1f} J={j:.1f}')

        j = j + 1
    i = i + a
    j = i + 1

