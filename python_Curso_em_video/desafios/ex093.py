jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))

for c in range(0, partidas):
    gol= int(input(f'Quantos gols na {c+1} partida?: ')) 
    gols.append(gol)

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)


print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')


for i, g in enumerate(gols):
    print(f'Na partida {i+1}, fez {g} gols.'.center(40))
print(f'Foi um total de {jogador["total"]} gols que {jogador["nome"]} fez!')