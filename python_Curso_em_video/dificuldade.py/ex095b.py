jogador = {}
time = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    quant = int(input(f'quantas partidas {jogador["nome"]} jogou?: '))
    gols = []
    for c in range (quant): 
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na {c+1}ª partida?: ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
        


    while True:
        escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
        if escolha in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if escolha == 'N':
        break


print('-='*30)

print(f'{"cod":<4} {"Nome":<15} {"Gols":<20} {"Total":>7}')
print('-'*60)

for i, v in enumerate(time):
    print(f'{i:<4} {v["nome"]:<15} {str(v["gols"]):<20} {v["total"]:>5}')
print('-'*60)

while True:
    ver = int(input('Mostrar dados de qual jogador? (999 pra parar!): '))
    if ver == 999:
        break
    if ver >=len(time):
        print('Erro! jogador invalido!')

    else:   
        jogador = time[ver]
        print(f'-- LEVANTAMENTO DE DADOS DO JOGADOR: {jogador["nome"]}')
        for i, g in enumerate(jogador["gols"]):
            print(f'no jogo {i+1} fez {g} gols!')
