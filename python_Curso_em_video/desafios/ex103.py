def jogador(nome="<desconhecido>", gols=0):
    return f'O jogador {nome} fez {gols} gols no campeonato!'

nome = input('Nome: ')
gols = input('Gols: ')

if nome.strip() == '':
    nome = "<desconhecido>"
if not gols.isnumeric():
    gols = 0
else:
    gols = int(gols)

print(jogador(nome, gols))

