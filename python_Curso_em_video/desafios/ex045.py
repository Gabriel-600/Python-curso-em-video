from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print ('''
[0]PEDRA
[1]PAPEL
[2]TESOURA

''')

jogador = int(input('Qual é a sua jogada? ')) 
print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print ('-='*10)
print ('O jogador jogou {}'.format(itens[jogador]))
print ('O computador jogou {}'.format (itens[computador]))
print ('-='*10)

if computador == 0: #computador jogou pedra
    if jogador == 0: 
        print ('EMPATE!')
    
    elif jogador == 1:
        print ('VOCÊ VENCEU!')

    elif jogador ==2:
        print('COMPUTADOR VENCEU!')

    else:
        print ('Jogada invalida!')
    
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print ('COMPUTADOR VENCEU!')

    elif jogador == 1:
        print('EMPATE')
    
    elif jogador == 2:
        print('VOCÊ VENCEU!')

    else:
        print('Jogada invalida!')

elif computador ==2: #computador jogou tesoura

    if jogador == 0:
        print('VOCÊ VENCEU!')

    elif jogador ==1:
        print('COMPUTADOR GANHOU!')

    elif jogador ==2:
        print('EMPATE!')

    else:
        print('Jogada invalida!')