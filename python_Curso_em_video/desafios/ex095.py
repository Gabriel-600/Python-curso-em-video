time = []
jogador = {}

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou?: '))

    gols = []
    for c in range (0, jogos):
        gols.append (int(input(f'Quantos gols {jogador["nome"]} fez na {c+1}ª partida?: ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())

    while True:
        escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
        if escolha in 'SN':
            break
        print('Erro! escolha apenas S ou N!')
    if escolha =='N':
        break

print('-='*30)
print(f'{"cod":<4} {"Nome":<15} {"Gols":<20} {"Total":>5}')
print('-'*60)
for i, v in enumerate(time):
    print(f'{i:<4} {v["nome"]:<15}  {str(v["gols"]):<20} {v["total"]:<5}')
print('-'*60)


while True:
    esc = int(input('Mostrar dados de qual jogador? (999 pra parar!): '))
    if esc == 999:
        break
    if esc >= len(time):
        print(f'Erro! não existe jogador com o codigo {esc}')
    else:
        jogador = time[esc]
        print(f'levantamento de dados do jogador: {jogador["nome"]}')
        for i, g in enumerate(jogador["gols"]):
            print(f'   No jogo {i+1} fez {g} gols!')
print('-='*30)
print('<< VOLTE SEMPRE >>')