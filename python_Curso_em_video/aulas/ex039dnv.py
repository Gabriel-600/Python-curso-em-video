from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento'))
idade = atual - nasc
print ('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade ==18:
    print('Você tem que se alistar IMEDIATAMENTE! ')

elif idade <18:
    saldo = 18 - idade
    print ('ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print ('Seu alistamento vai ser em {}'.format(saldo))

elif idade > 18:
    saldo = idade - 18
    print ('Voce deveria ter se alistado a {} anos atras!'.format(saldo))
    ano = atual + saldo 
    print ('Seu alistamento foi em {}'.format(ano))