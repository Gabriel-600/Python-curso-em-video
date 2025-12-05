from random import randint

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range (0,5):
        n = randint(1,10)
        lista.append(n)
        print(n, end=' ')
    print('>> PRONTO! ')


def soma_par(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'\nA soma dos numeros pares da lista {lista} é {soma}')



numeros = []
sorteia(numeros)
sorteia()
soma_par(numeros)