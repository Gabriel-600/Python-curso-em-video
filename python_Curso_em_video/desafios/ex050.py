soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite o {} numero: '.format(c)))
    if num % 2 ==0:
        soma = soma + num
        cont += 1
print ('A soma entre os {} numeros pares é {}'.format(cont, soma))