from time import sleep
from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

rank = {}

for k, v in jogo.items():
    print(f'O {k} tirou {v}')
rank = sorted(jogo.items(),key=itemgetter(1), reverse=True)
print('-='*30)
print('== RANK DE JOGADORES =='.center(40))
for i, v in enumerate(rank):
    print(f'{i+1}º Lugar foi {v[0]} com {v[1]}'.center(40))