lista = []
temp = []
while True:
    temp.append (str(input('Nome: ')))
    temp.append (float(input('Nota1: ')))                               #lista.append([nome, [nota1, nota2], media])
    temp.append (float(input('Nota2: ')))
    lista.append(temp[:])
    temp.clear()

    escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
    while escolha not in 'SN':
        print('Escolha invalida, tente novamente! ', end='')
        escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
    if escolha == 'N':
        break

print('-='*30)
print(f'{"N":<3} {"Nome":<5} {"Média":>15}')     # print(f'{"N":<3} {"Nome":<10} {"Média":>8}')

print('-'*30)
for pos , nt in enumerate(lista):
    print(f'{pos:<3} {nt[0]:<5} {(nt[1] + nt[2]) / 2:>15}')
print('-'*30)

while True:
    qual = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for pos, nt in enumerate(lista):
        if qual == pos:
            print(f'A nota de {nt[0]} foi {nt[1]} e {nt[2]}')
        if qual >= len(lista):
            print('Numero invalido! Tente novamente.')
    if qual == 999:
        break
print('-'*30)
print('ENCERRANDO...')



'''while True:
    qual = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if qual == 999:
        break
    if qual >= len(lista):
        print('Número inválido! Tente novamente.')
    else:
        print(f'Notas de {lista[qual][0]}: {lista[qual][1]} e {lista[qual][2]}')
'''