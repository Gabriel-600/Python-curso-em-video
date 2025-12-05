def fatorial(num=1, show=False):
    """Calcula o fatorial do numero 

    Args:
        num (int, optional): Numero a ser calculado Defaults to 1.
        show (bool, optional): Se for True mostra o calculo! Defaults to False.

    Returns:
        int: O valor do fatoral num
    """
    f = 1
    for c in range(num,0,-1):
        f *= c
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x', end=' ')
            else:
                print(' =',end=' ')
    return f



print('-'*20)
print(fatorial(5, show=True))
