y=int(input('Введите значение y: '))
a=int(input('Введите значение a: '))
p=int(input('Введите значение p: '))

for x in range(0,p):
    if (a**x)%p==y:
        print("x =", x)
        break
