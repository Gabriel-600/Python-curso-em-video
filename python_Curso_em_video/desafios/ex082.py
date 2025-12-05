valores = []
pares = []
impar = []

while True:
    num = int(input('Digite um numero! '))
    valores.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impar.append(num)
         
    escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
    while escolha not in "SN":
        print('Escolha invalida! ', end='')
        escolha = str(input('Quer continuar? [S/N]: ')) .strip() .upper()[0]
    if escolha == 'N':
        break

print('-='*30) 

print(f'Os Numeros digitados foram: {valores}')
print(f'Os Numeros pares digitados foram: {pares}')
print(f'Os Numeros impares digitados foram: {impar}')






'''
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)'''       #Guanabara fez assim