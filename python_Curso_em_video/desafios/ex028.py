from random import randint
from time import sleep

computer = randint(0, 5) # faz o computador pensar
print ('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5 Tente adivinhar...')
print ('-=-' *20)
jogador = int(input('Em que numero eu pensei? '))
print ('PROCESSANDO...')
sleep(2)
if jogador == computer:
    print ('ACERTOU')

else:
    print ('Errou eu pensei no numero {}'.format(computer))