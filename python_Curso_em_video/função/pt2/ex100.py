from random import randint


def sorteia(lista):
    print('Sorteando 5 numeros: ', end='')
    for n in lista:
        print(n,end=' ')    
    for c in range (0, 5):
        num = randint(0, 10)
        lista.append(num)
    print(lista, end=' ')
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'\nOs numeros pares da lista {lista} são {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)