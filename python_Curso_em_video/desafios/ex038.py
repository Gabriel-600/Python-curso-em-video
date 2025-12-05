n1 = int(input('Digite um Numero: '))
n2 = int(input('Digite mais um Numero: '))

if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))

elif n2 > n1:
    print('{} é maior que {}! '.format(n2, n1))

else:
    print ('Os numeros {} e {} são iguais! '.format(n1, n2))