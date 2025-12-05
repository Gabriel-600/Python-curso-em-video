casa = float(input('Digite o valor da casa? '))
salario = float(input('Digite seu salario R$ '))
anos = int(input('Digite em quantos anos pretende pagar: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print ('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='')
print ('a prestação sera de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo concedido!')

else:
    print('Emprestimo negado!')
    