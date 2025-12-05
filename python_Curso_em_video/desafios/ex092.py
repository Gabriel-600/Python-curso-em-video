from datetime import datetime
trabalhador = {}

anoatual = datetime.now().year  

trabalhador['nome'] = str(input('Nome: '))
nascimento = int(input('ano de nascimento: '))
trabalhador['idade'] = anoatual - nascimento        
trabalhador['carteira'] = int(input('Carteira de trabalho (0 se não tem!): '))

if trabalhador['carteira'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salario:  R$ '))

    aposentadoria = trabalhador['contratação'] + 35 
    trabalhador['aposentadoria'] = aposentadoria - nascimento

print('-='*30)

for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}!')

print('-='*30)
print('FIM!'.center(40))



#ASSIM O FINAL FICA MAIS BONITO!
'''print('-='*30)
print(f'Nome: {trabalhador["nome"]}')
print(f'Idade: {trabalhador["idade"]} anos')

if trabalhador['carteira'] == 0:
    print('Não possui carteira de trabalho.')
else:
    print(f'CTPS: {trabalhador["carteira"]}')
    print(f'Ano de contratação: {trabalhador["contratação"]}')
    print(f'Salário: R$ {trabalhador["salario"]:.2f}')
    print(f'Aposentadoria aos {trabalhador["aposentadoria"]} anos de idade.')'''