from random import randint
cont = 0
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados foram:',end=' ' )
for numero in tupla:
    print(f'{numero}', end=' ' )

print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor numero sorteado foi {min(tupla)}')




#OU

# Percorre a tupla comparando
'''for numero in tupla:
    if numero > maior:
        maior = numero
    if numero < menor:   
        menor = numero
        '''