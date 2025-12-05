from datetime import datetime
trabalhador = {}
anoatual = datetime.now().year
trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = int(input('Ano de nascimento: '))
trabalhador['idade'] = anoatual - trabalhador['idade']
trabalhador['cttps'] = int(input('Carteira de trabalho (0 se não ter!): '))

if trabalhador['cttps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salario: R$'))
    aposentadoria = trabalhador['contratação'] + 35
    trabalhador['aposentadoria'] = aposentadoria - trabalhador['idade']
print('-='*30)

for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')