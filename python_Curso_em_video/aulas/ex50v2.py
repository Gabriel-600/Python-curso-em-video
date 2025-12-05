somaimpa = 0
somapar = 0
for c in range (1,7):
    num = int (input('Digite o {} valor: '.format(c)))
    if num % 2 ==0:
        somapar += num
    else:
        somaimpa +=num
print ('a soma dos numeros pares é {}'.format(somapar))
print ('A soma dos numeros impares é {}'.format(somaimpa))