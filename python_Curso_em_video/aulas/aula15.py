num = cont = soma = 0

while True:
    num = int(input('Digite um numero: '))
    if num == 999:
     break
    cont += 1
    soma += num
    
print(f'A soma de {cont} numeros deu {soma}')
print('FIM!')


