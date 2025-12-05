from random import randint
jogador = {}
play = []
quant = int(input('Quantos vaõ jogar?: '))

for c in range(1, quant+1):
    jogador['nome'] = str(input(f'Nome do {c}º jogador: '))
    jogador['pontos'] = int(input(f'Quantos pontos {jogador["nome"]} fez?: '))
    play.append(jogador['nome'])
    play.append(jogador['pontos'])

print('-='*20)
for k, v in jogador.items():
    print(f'O jogador {k} fez {v} pontos!')