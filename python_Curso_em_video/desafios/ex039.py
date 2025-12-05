idade = int(input('Digite sua idade: '))
falta = 18 - idade
passou = idade - 18

if idade == 18:
    print ('Você precisa se alistar! ')

elif idade <18:
     print('Quando tiver 18 anos você se alistara! ainda falta {} ano(s)! '.format(falta))

else:
     print ('Ja passou {} anos do tempo de se alistar!! '.format(passou))