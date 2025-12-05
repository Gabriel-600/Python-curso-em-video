lista = []

for valor in range(0,6):
    lista.append(int(input(f'Digite um numero para a posição {valor}: ')))
    

maior = max(lista)
menor = min(lista)

print('=-'*20)
print(f'Você digitou os valores {lista}')


print(f'O maior valor foi {maior} na posição: ',end='')
for pos,num in enumerate(lista):
    if num == maior:
        print(pos)

print(f'O menor valor foi {menor} na posição: ', end='')
for pos, num in enumerate(lista):
    if num == menor:
        print(pos)