from random import randint
from time import sleep
from operator import itemgetter

jogador = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}
rank = []

for k, v in jogador.items():
    print(f'O {k} tirou {v} no dado!')
    sleep(1)



print('-='*30)
print('== RANKING DE JOGADORES! == '.center(40))
rank = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'{i+1}º lugar {v[0]} com {v[1]}.'.center(40))

