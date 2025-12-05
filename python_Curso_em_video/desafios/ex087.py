matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = mai = scol = 0 
for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha] [coluna] = int(input(f'Digite um valor para [{linha}], [{coluna}]: '))

print('-='*30)
for linha in range (0,3):
    for coluna in range (0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
    print()

print('-='*30)

print(f'A soma dos numeros pares {pares}')
for l in range (0,3):
    scol += matriz [linha][2]
print(f'A soma dos valores da terceira coluna é {scol}')

for c in range (0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha {mai}')