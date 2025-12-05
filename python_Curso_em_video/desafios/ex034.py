salario = float(input('Digite seu salario! '))
maior = salario * 15 / 100
menor = salario *10 / 100
novo1 = salario + maior
novo2 = salario + menor

if salario <=1250:
    print ('O aumento foi de {:.2f} e seu novo salario é {}'.format(maior, novo1))


else: 
    print ('O aumento foi de {:.2f} e seu novo salario é {}'.format(menor, novo2))