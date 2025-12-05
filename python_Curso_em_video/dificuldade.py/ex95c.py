jogador = {}
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))  
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou?: '))

    gol = []
    for c in range(partidas):
        gol.append(int(input(f'   Quantos gols {jogador['nome']} fez na {c+1} partida?: ')))

    jogador['gols'] = gol[:] 
    jogador['total'] = sum(gol)
    time.append(jogador.copy())



        #CONTINUAR
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if continuar == 'N':
        break

print('-='*30)

print(f'{"cod":<4} {"Nome":<15} {"gols":<20} {"Total":>5}')
for i, v in enumerate(time):
    print(f'{i:<4} {v["nome"]:<15} {str(v[("gols")]):<20} {v["total"]:>4}')

while True:
    ver = int(input('Quer ver detalhes de qual jogador?: [999 pra parar!]: '))

    if ver == 999:
        break
    if ver >= len(time):
        print('ERRO! Não existe jogador com esse codigo!')

    else:
        jogador = time[ver]
        for i, v in enumerate(jogador["gols"]):
            print(f'-- Na partida {i+1} fez {v} gols!')
print('-'*30)
print('<<< VOLTE SEMPRE >>>'.center(40))