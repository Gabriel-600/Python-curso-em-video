''' 
aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

print('-='*20)

print(f'O nome do aluno é {aluno["nome"]}')
print(f'A media do {aluno["nome"]} é {aluno["media"]}!')                    #guanabara fez diferente

if aluno['media'] >= 7:
    print(f'Aluno {aluno["nome"]} foi Aprovado!')

elif aluno['media'] >= 5:
    print(f'Aluno {aluno["nome"]} Esta de recuperação!')

else:
    print(f'Aluno {aluno["nome"]} foi reprovado!') '''


aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >=7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >=5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-='*20)
for k, v in aluno.items():
    print(f'{k}: {v}'.center(40))  
print('-='*20)
