from random import randint


def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for c in range(0,5):
        n = randint(0,10)
        numeros.append(n)
        print(n, end=' ')
    print('PRONTO!')


def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma entre os numeros pares {lista} da o resultado {soma}')




numeros = []

sorteia(numeros)
soma_par(numeros)




























'''from random import randint

def sortear(lista):
    print('Sorteando os 5 valores para a lista: ', end=' ')
    for c in range(0,5):
        numeros = randint(0,10)
        lista.append(numeros)
        print(f'{numeros}', end=' ')
    print('PRONTO!')


def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos pares da lista {lista} da o resultado {soma}')


numeros = []
sortear(numeros)
soma_par(numeros)
'''
