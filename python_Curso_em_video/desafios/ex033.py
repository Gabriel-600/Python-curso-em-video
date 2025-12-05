num1 = int(input('Digite o primeiro numero! '))
num2 = int (input('Digite o segundo numero! '))
num3 = int(input('Digite o terceiro numero! '))

if num1 > num2 and num1 > num3:
    print ('O maior numero é {}'.format(num1))

if num2 > num1 and num2 > num3:
    print ('O maior numero é {}'.format (num2))

else:
    print ('O maior numero é {}'.format(num3))






    # Lendo os três números
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

# Descobrindo o maior
if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n3:
        maior = n2
    else:
        maior = n3

# Descobrindo o menor
if n1 < n2 and n1 < n3:
    menor = n1
else:
    if n2 < n3:
        menor = n2
    else:
        menor = n3

# Mostrando os resultados
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
