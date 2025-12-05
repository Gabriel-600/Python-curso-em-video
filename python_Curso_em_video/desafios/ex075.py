a = int(input("Digite o 1º valor: "))
b = int(input("Digite o 2º valor: "))
c = int(input("Digite o 3º valor: "))
d = int(input("Digite o 4º valor: "))
pares = 0
tupla = (a, b, c, d)


print("Os valores digitados foram: ", tupla)
print('-'*50)
print(f'O numero 9 apareceu:{tupla.count(9)} vezes')
print('-'*50)
if 3 in tupla:
    print('O primeiro valor 3 ta na posição:',tupla.index(3)+1)
else:
    print('O valor 3 não foi digitado! ')
    print('-'*50)
print('Os numeros pares digitados foram: ',end='')
for n in tupla:
    if n % 2 == 0:       
        print(n ,end=',')
        pares += 1
