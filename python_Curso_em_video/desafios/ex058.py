from random import randint
from time import sleep
tentativa = 0
computer = randint(0, 5)
print ('='*37)
print('Tente adivinhar o numero que pensei!')
print ('='*37)

jogador = int(input('Qual numero eu pensei? '))
while jogador != computer:
    print('Processando...')
    sleep(1)
    print('ERROUUUU, TENTE NOVAMENTE NÃO DESISTA!')
    tentativa += 1
    jogador = int(input('Digite outro numero: '))
tentativa += 1 
print ('PARABENS!!!')
print('Você digitou: {}, O Computador pensou:{}, Precisou de {} tentativas'.format(jogador, computer, tentativa))