from random import randint
from time import sleep

def sortear():
    print('-='*30)
    lista = [randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)]
    print(f'Sorteando {len(lista)} valores da lista: ', end='')
    
    for v in lista:
        sleep(0.4)
        print(f'{v}', end=' ')
    print('PRONTO!')
    return lista

def pares():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma = soma + n 
    print(f'\nSomando os numeros pares de {numeros} temos: {soma}')
 
numeros = sortear()
pares()