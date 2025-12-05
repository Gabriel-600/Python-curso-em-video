from datetime import datetime

trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['carteira'] = int(input('Carteira de trabalho (0 se não tiver): '))
if trabalhador['carteira'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salario: '))

    aposentadoria = trabalhador['contratação'] + 35
    trabalhador['aposentadoria'] = aposentadoria - nasc
print('-='*30)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')