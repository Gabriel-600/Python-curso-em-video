peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
alt = altura * altura
imc = peso / alt

if imc <=18.5:
    print ('Abaixo do peso! seu imc é {:.1f}'.format(imc))

elif imc <=25:
    print ('Peso ideal! seu imc é {:.1f}'.format(imc))

elif imc <=30:
    print ('Sobrepeso! seu imc é {:.1f}'.format(imc))

elif imc <=40:
    print ('Obesidade! seu imc é {:.1f}'.format(imc))

else:
    print ('Obesidade morbida! seu imc é {:.1f}'.format(imc))
