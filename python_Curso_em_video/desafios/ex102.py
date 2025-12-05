def fatorial(num=1, show =False):
    '''Calcula o fatorial de um número.
    num: O numero a ser calculado
    return: O valor do fatorial de num
    '''
    f = 1 
    for c in range(num, 0, -1):
        if show == True:
            print(c, end=' ')
            if c > 1:
                print('x', end= ' ')
            else:
                print('=', end=' ')

        f *= c
    return f 

print('-'*20)
print(fatorial(5, show=True))