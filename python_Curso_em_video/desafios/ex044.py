print('{:=^40}'.format('LOJAS HENRIQUE'))
preco = float(input('Preços das compras: R$'))


print (''' Formas de pagamento
[1] á vista dinheiro ou cheque
[2] á vista do cartão
[3] 2x no cartão
[4] 3x ou mais no cartão             
''' )
opcao = int(input('Qual a sua forma de pagamento? '))

if opcao == 1:
    total = preco - (preco *10 / 100)

elif opcao == 2: 
    total = preco - (preco * 5 / 100)

elif opcao == 3:
    total = preco
    parcela = preco /2
    print ('Sua compra sera parcelada em 2x de {:.2f} sem juros '.format(parcela))

elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print ('Sua compra sera parcelada em {}x de R${:.2f} com juros'.format(totalparc, parcela))


else:
    print('OPÇÃO INVALIDA! ')

print ('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, total))
    