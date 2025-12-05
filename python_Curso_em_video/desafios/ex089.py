notas = []
temp = []


while True:
    nome = str(input('Nome: '))
    temp.append(nome)
    nota1 = float(input('Nota1: '))
    temp.append(nota1)
    nota2 = float(input('Nota2: '))
    temp.append(nota2)
    media = (nota1 + nota2) / 2
    temp.append(media)
    notas.append(temp[:])
    temp.clear()
    


    escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()
    while escolha not in 'SN':
        print('Escolha invalida!', end='')
        escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()
    if escolha == 'N':
        break


print('-='*30)
#for pos ,n in enumerate(notas):
print(f'{"Nº":<4} {"NOME":<15} {"MEDIA":>8}')
print('-'*30)
for pos ,item in enumerate(notas):
    print(f'{pos:<4} {item[0]:<15} {item[3]:>5.1f}')
print('-'*30)

while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    if aluno < len(notas):
        print(f'Notas de {notas[aluno][0]} são {notas[aluno][1]} e {notas[aluno][2]}')

print('<<< VOLTE SEMPRE >>>')


'''while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    if aluno < len(notas):  # garante que o número existe
        print(f'Notas de {notas[aluno][0]} são {notas[aluno][1]} e {notas[aluno][2]}')
''' 