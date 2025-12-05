def ficha(nome='<<desconhecido>>', gols=0):
    print(f'O jogador {nome} fez {gols} gols!')

    
nome = str(input('Nome do jogador: '))
gols =  str(input('Gols: '))


if nome.strip() == '':
        nome ="<<desconhecido>>"
if gols.isnumeric():
      gols = int(gols)
else:
      gols = 0

      




ficha(nome, gols)
