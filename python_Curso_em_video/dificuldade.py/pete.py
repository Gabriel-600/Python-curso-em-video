from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6) }
rank = []
print('JOGO DE DADOS'.center(50))
print('-='*30)
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado!')
    sleep(0.7)

rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('RANKING DOS JOGADORES'.center(40))

for i, k in enumerate(rank):
    sleep(0.5)
    print(f'o {i+1}ºLugar foi {k[0]} com {k[1]} pontos!')