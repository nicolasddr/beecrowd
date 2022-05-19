
x = int(input())
y = int(input())

if x > y:
    a = y
    b = x
else:
    a = x
    b = y

for i in range(a+1, b):
    if i % 5 == 2 or i % 5 == 3:
        print(i)

