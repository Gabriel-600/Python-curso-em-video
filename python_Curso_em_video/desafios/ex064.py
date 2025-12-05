num = int(input('Digite um numero [Escreva 999 pra parar!] '))
soma = 0
cont = 0
while num != 999:
   soma += num 
   num = int(input('Digite um numero [Escreva 999 pra parar!] '))
   cont += 1
print('Você digitou {} numeros, a soma entre eles é {}'.format(cont, soma))     