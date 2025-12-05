from random import randint
from time import sleep
from operator import itemgetter

carros = {'Ferrari': randint(100, 400),
          'Porshe': randint(100, 400),
          'lambo': randint(100,400),
          'fusca': randint(100,400)}

rank = {}

for k, v in carros.items():
    print(f'O carro {k} atingiu {v} km/h!')
    sleep(1)

print('-='*20)
print('== RESULTADO DA CORRIDA =='.center(40))

rank = sorted(carros.items(), key=itemgetter(1) , reverse=True)

for i, v in enumerate(rank):
    print(f'{i+1}º lugar foi {v[0]} atingindo {v[1]} km/h!'.center(40))

print('-='*20)