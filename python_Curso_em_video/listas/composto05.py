from random import randint
lista = []
jogos = []
cont = 0
tot = 1
print('-'*30)
print('      JOGO NA MEGA SENA       ')
print('-'*30)


quant = int(input('Quantos jogos? '))
while tot <= quant:
    while True:
        sorteio = randint(1 ,60)
        if sorteio not in lista:
            lista.append(sorteio)
            cont += 1
        if cont >= 6:
            break 
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print(f'Os numeros sorteados foram {jogos}')



'''from random import randint
from time import sleep

lista = []
jogos = []

print('-' * 30)
print('      JOGO NA MEGA SENA       ')
print('-' * 30)

quant = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)

for c in range(quant):
    lista = []
    while len(lista) < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogos.append(lista)
    print(f'Jogo {c+1}: {lista}')
    sleep(0.5)  # pausa de meio segundo pra dar sensação de "sorteio"

print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
'''