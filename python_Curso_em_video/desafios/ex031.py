viagem = float(input('Qual a distancia da viagem em km? '))
km200 = viagem * 0.50
km201 = viagem * 0.45
print ('Sua viagem será de {}km, então o valor sera: '.format(viagem))
if viagem <=200:
    print ('Sua viagem custara R${:.2f}'.format(km200))

else:
    print ('Sua viagem custara R${:.2f}'.format(km201))