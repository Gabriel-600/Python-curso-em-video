'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        print(c, end=' ')
        print('x ' if c > 1 else '= ', end='')
        f *= c
    print(f'{f}')

fatorial(5)'''

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()


print(f'{f1}, {f2} e {f3}')