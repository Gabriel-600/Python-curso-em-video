numeros = []

for n in range(0,6):
    numeros.append(int(input(f'Digite um valor para a posição {n}: ')))

print(numeros)
print('=-'*40)

maior = max(numeros)
menor = min(numeros)


print(f'O maior valor foi: {max(numeros)} nas posições: ',end=' ')
for pos, valor in enumerate(numeros):
    if valor == maior:
        print(pos, end=',')

    
print(f'\nO menor valor foi {menor} nas posições: ',end=' ')
for pos, valor in enumerate(numeros):
    if valor == menor:
        print(pos, end=',')
