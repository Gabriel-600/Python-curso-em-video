num = cont = soma = 0

while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1

print (f'A soma de {cont} numeros é igual a {soma}')
