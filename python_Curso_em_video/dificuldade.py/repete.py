aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))


if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado!'

elif aluno['media'] >=5 and aluno['media'] < 7:     # elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação!'

else:
    aluno['situação'] = 'Reprovado!'
 
print('-='*30)

for k, v in aluno.items():
    print(f'{k} é igual {v}')